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
