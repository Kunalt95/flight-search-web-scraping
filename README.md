## Web scraping - Cheapest Flight Price
There is 3 main parts to this project. 

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

 
![Final Product](https://lh3.googleusercontent.com/fw2-yCqHIcoU64qpQ_Ay19Tv_PRg0mzEgGc9jeK4XARq_QPcYWOisu0KYkyLiX1BnKg8KcJkD5EXa9b3DWrNV58KQ_YU2xylZvB26-vtGwMGVuJsfs9lUusmTCl-fWX0yKY7z9iKcgKtieb7HILlCBHG1J1wzdz143t8iO82fRYI1YsJuSfwKezpcpytnwybHA5Qj5FnwuNnnVx7l7pzDE7r0Zw8mujGiOsdqBHoSO4nC7K8cLgoNYRNX6gdmFVq-3ISuvxoKQkYvVZOyOplm7OMmHFqWa1AIvTNbZg7s_grpSGMe1DS-RcGu0RJXNDSOmbWLzesJOEPHxcI6DQED1nLlEXQTHrISPxKThGJfynrFxorObfUl2lhKKha1s_ieYY3ZVhANZtfHtA-wZx5gR_LR2D_bk828inc3qhxQCvm6guXXZP2mPXN2NcpmOyzN2B0cWs4x4dennTsFL3LgkvLWdj1oJjD5tQn7zjUw1a0qNF479Goxk8ckOprCrIINPrfF4C8NBoevxnVBG7slaJWHsM7gcyq1LFXdIVBGM6mGe_QZVYCg7awmljUdlPfC1sfpufE1TZGf1CeJ8ruRimpnMd9-Dcq0shfz_yw1ibqaHPWan0fkPqI9bNne_TPnZH_LNDAPN0xQCVkfk0QHe95FvsDDUHWyXtTDpmnwAXBhMQmvKjJVbw=w2366-h1250-no)
