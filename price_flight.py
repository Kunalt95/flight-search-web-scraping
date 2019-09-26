from selenium import webdriver
from bs4 import BeautifulSoup
import re
import time
import sqlite3

# from_loc = input("Flying from: ")
# from_to = input("Flying to: ")
# date = input("What date (dd/mm/yyyy): ")

from_loc = "Dublin"
from_to = "london"
date = "22/11/2019"


url = f"https://www.expedia.ie/Flights-Search?trip=oneway&leg1=from:{from_loc},to:{from_to},departure:{date}TANYT&passengers=adults:1,children:0,seniors:0,infantinlap:Y&options=cabinclass:economy&mode=search&origref=www.expedia.ie"

print(f"URL: {url}")
print("The cheapest flights: \n")

driver = webdriver.Firefox()
driver.get(url)
time.sleep(10)
soup = BeautifulSoup(driver.page_source, 'lxml')
driver.quit()

# Getting all the data from the website using html elements and tags.
airline_name = soup.find_all('span', attrs={'data-test-id': 'airline-name'})
duration = soup.find_all('span', attrs={'class': 'duration-emphasis'})
stops = soup.find_all('span', attrs={'class': 'number-stops'})
depart_times = soup.find_all('span', attrs={'data-test-id': 'departure-time'})
arrival_times = soup.find_all('span', attrs={'data-test-id': 'arrival-time'})
price = soup.find_all('span', attrs={'data-test-id': 'listing-price-dollars'})

# Cleaning up the data, such as getting only text and removing whitespace. This all gets stored in list using list comprehension.
airlines_name_list = [a.getText().strip() for a in airline_name]
flight_durations = [b.getText().strip() for b in duration]
flight_stops = [c.getText().strip() for c in stops]
price_list = [d.getText().strip() for d in price]
depart_list = [e.getText().strip() for e in depart_times]
arrival_list = [f.getText().strip() for f in arrival_times]

# Removing the euro symbol and commas so data can be converted to int from str
num_price_list = [int(re.sub('[€,]', '', x)) for x in price_list]


zipped_list = zip(airlines_name_list, depart_list, arrival_list, flight_durations, flight_stops, num_price_list)

conn = sqlite3.connect("flight_search.db")
c = conn.cursor()
# c.execute("CREATE TABLE cheap_flights (airlines TEXT, depart_time TEXT, arrival_time TEXT, duration TEXT, stops TEXT, price INTEGER)")

for data in zipped_list:

    if data[5] == min(num_price_list):
        print(data)
        query = f"INSERT INTO cheap_flights VALUES (?, ?, ?, ?, ?, ?)"
        c.execute(query, data)
        conn.commit()

conn.close()
