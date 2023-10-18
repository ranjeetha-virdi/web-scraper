# Develop a Webscraper using Scrapy
### Objective: 
The objective for this scraping system is to monitor property postings for property website Immobillienscout and scarp the data for each property posted.
### Required Data: 
We want to scrape property features like price, address,nos of rooms, living space etc and store the relevant information.

````
├── scrapy.cfg
└── propscraper
    ├── __init__.py
    ├── items.py
    ├── middlewares.py
    ├── pipelines.py
    ├── settings.py
    └── spiders
        └── __init__.py
        └── immoscraper.py
````
### Scale: 
This will be a relatively small scale scraping process (hundreds of keywords), so no need to design a more sophisticated infrastructure.
### Data Storage: 
To store the scraped data to a PostgresSQL Database.
## Step 1: Understand immobilienscout24.de web pages.
For example, here is how we would get search results for flats for rent in Munich.
````
unencoded : https://www.immobilienscout24.de/Suche/de/bayern/muenchen/wohnung-mieten?enteredFrom=one_step_search
encoded : https%3A%2F%2Fwww.immobilienscout24.de%2FSuche%2Fde%2Fbayern%2Fmuenchen%2Fwohnung-mieten%3FenteredFrom%3Done_step_search
````

This URL contains a number of parameters that we will explain:

    /de/bayern/muenchen/wohnung-mieten: Here the country : **de**, state: **bayern**, city:  **muenchen** and finally we are searching a flat to rent i.e indicated by **wohnung-mieten**
    l stands for the location you want to search for jobs. In our case, we used l=California.
    start stands for the starting point for the pagination. We use the start parameter to paginate through results. 
