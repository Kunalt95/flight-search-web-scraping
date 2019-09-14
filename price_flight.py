from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

from_loc = input("Flying from: ")
from_to = input("Flying to: ")
date = input("What date (dd/mm/yyyy): ")

url = f"https://www.expedia.ie/Flights-Search?trip=oneway&leg1=from:{from_loc},to:{from_to},departure:{date}TANYT&passengers=adults:1,children:0,seniors:0,infantinlap:Y&options=cabinclass:economy&mode=search&origref=www.expedia.ie"

print(url)
print("Results: ")

driver = webdriver.Firefox()
driver.get(url)
WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.CLASS_NAME, "duration-emphasis")))
soup = BeautifulSoup(driver.page_source, 'lxml')

# Getting all the date from the website using html elements and tags.
airline_name = soup.find_all('span', attrs={'data-test-id': 'airline-name'})
duration = soup.find_all('span', attrs={'class': 'duration-emphasis'})
stops = soup.find_all('span', attrs={'class': 'number-stops'})
depart_times = soup.find_all('span', attrs={'data-test-id': 'departure-time'})
arrival_times = soup.find_all('span', attrs={'data-test-id': 'arrival-time'})
price = soup.find_all('span', attrs={'data-test-id': 'listing-price-dollars'})

# Cleaning up the data, such as getting only text and removing whitespace.
airlines_name_list = [a.getText().strip() for a in airline_name]
flight_durations = [b.getText().strip() for b in duration]
flight_stops = [c.getText().strip() for c in stops]
price_list = [d.getText().strip() for d in price]
depart_list = [e.getText().strip() for e in depart_times]
arrival_list = [f.getText().strip() for f in arrival_times]


test = [print(item, "\n") for item in zip(airlines_name_list, depart_list, arrival_list, flight_stops, price_list)]

driver.quit()
