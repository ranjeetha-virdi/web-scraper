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
1. For example, here is how we would get search results for flats for rent in Munich.
````
unencoded : https://www.immobilienscout24.de/Suche/de/bayern/muenchen/wohnung-mieten?enteredFrom=one_step_search
encoded : https%3A%2F%2Fwww.immobilienscout24.de%2FSuche%2Fde%2Fbayern%2Fmuenchen%2Fwohnung-mieten%3FenteredFrom%3Done_step_search
````

This URL contains a number of parameters that we will need to understand inorder to paginate/navigate through the pages of the website:
````
    /de/bayern/muenchen/wohnung-mieten: 
     |   |        |        └── flat to rent **wohnung-mieten**
     |   |        └── city:  **muenchen** 
     |   └── state: **bayern**                     
     └── country : **de** 
````  
2. Similarly if we want to scrape properties for sale then here is how we would get search results for flats for sale in Munich.
````
unencoded : https://www.immobilienscout24.de/Suche/de/bayern/muenchen/wohnung-kaufen?enteredFrom=one_step_search
encoded : https%3A%2F%2Fwww.immobilienscout24.de%2FSuche%2Fde%2Fbayern%2Fmuenchen%2Fwohnung-kaufen%3FenteredFrom%3Done_step_search
````

This URL contains a number of parameters that we will need to understand inorder to paginate/navigate through the pages of the website:
````
    /de/bayern/muenchen/wohnung-kaufen: 
     |   |        |        └── flat to rent **wohnung-kaufen**
     |   |        └── city:  **muenchen** 
     |   └── state: **bayern**                     
     └── country : **de** 
````  
3. Using these parameters we can customise our requests to the property search endpoint to either scrape overall property data data or get property URLs that we can scrape individually.

With immobilienscout24.de it is very easy to extract the data that we need as the data is available as hidden JSON data on the page.All the listings are actually contained in the tag resultList, which further contains resultlistEntry which stores an array of 20 property listings

![js_obj](https://github.com/ranjeetha-virdi/web-scraper/assets/81987445/926e002c-1e94-4ad8-a9a5-b3f3608a4bf5)

So get at this data we can just use a regex command to find the window.IS24["resultlistEntry"] json on the page and parse it's contents.

## step 2: Build property Scraper:
So the first thing we need to do is to build a Scrapy spider that will send a request to the immobilien page,This will extract all the properties id from the property website page, create & request to url of each property with its id, and then trigger a parse_job scraper when it recieves a response. The data scrapped is stored in PostgresSQL database.


