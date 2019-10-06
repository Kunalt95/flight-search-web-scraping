## Web scraping - Cheapest Flight Price

This started out with me just creating a python script to get cheap flight results using web scraping (something I was trying to learn). Then invovled into storing data and then finally exposing that data on a web application. 

There are 3 main parts to this project. 

  **1. Python Script**: This ask users for 3 main inputs (from, to, date), then based on the input it generates Expedia flight search URL. Then using Selenium WebDriver I open that URL, from there I use BeautifulSoup to dig through the HTML code of the website to find necessary information, such as airline names, duration of flight, stops, timings, and price. After I do some data cleaning (getting rid of certain symbols, whitespace...etc.), which then allows me to loop through the returned flights to find the cheapest ones. 
  
  **2. SQL Database**: Created a database (`flight_search.db`) within the python script using SQLite3. Every time the script runs, it adds the cheapest flight(s) into the table.
  
  *SQL Table Schema*: ```c.execute("CREATE TABLE cheap_flights (date TEXT, from_city TEXT, to_city TEXT, airlines TEXT, depart_time TEXT, arrival_time TEXT, duration TEXT, stops TEXT, price INTEGER)")```
  
  
  **3. Ruby on Rails**: Created a simple rails project, here I saved the database from step-2, so the table within it could accessed via the flights controller. Then I displayed the contents of the table via HTML and CSS (bootstrap).
  
  
## Technologies

- The programming language of choice here was Python 3
- SQLite3
- Ruby on Rails (MVC Framework)
- Selenium
- BeautifulSoup (bs4)
- HTML and CSS

## Demo

1. Running the python script: 
![script](https://i.imgur.com/uzsKHj2.png)

2. Seeing the results being updated on the web application:
![website](https://i.imgur.com/6leCtje.png)
