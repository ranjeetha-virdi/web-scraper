# Develop a Webscraper using Scrapy
### Objective: 
The objective for this scraping system is to monitor property postings for property website Immobillienscout and scarp the data for each property posted.
### Required Data: 
We want to scrape property features like price, address,nos of rooms, living space etc and store the relevant information.

├── scrapy.cfg
└── myproject
    ├── __init__.py
    ├── items.py
    ├── middlewares.py
    ├── pipelines.py
    ├── settings.py
    └── spiders
        └── __init__.py
        └── immoscraper.py
