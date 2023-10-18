# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PropscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    immo_id = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    address = scrapy.Field()
    city = scrapy.Field()
    zip_code = scrapy.Field()
    district = scrapy.Field()
    contact_name = scrapy.Field()
    media_count = scrapy.Field()
    lat = scrapy.Field()
    lng = scrapy.Field()
    sqm  = scrapy.Field()
    rent = scrapy.Field()
    rooms = scrapy.Field()
    extra_costs = scrapy.Field()
    kitchen = scrapy.Field()
    balcony = scrapy.Field()
    garden = scrapy.Field()
    private = scrapy.Field()
    area = scrapy.Field()
    cellar = scrapy.Field()
    price = scrapy.Field()
    realtor = scrapy.Field()
