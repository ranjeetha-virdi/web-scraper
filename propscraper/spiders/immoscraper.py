import json
import scrapy
from urllib.parse import urljoin
import re


class ImmoCrawlSpider(scrapy.Spider):
    name = "immoscraper"
    

    def start_requests(self, offset=0):
        #state_list = ['bayern']
        city_list = ['muenchen']
        #todo_list = ['wohnung-kaufen']
        #for state in state_list:
        for city in city_list:
            #for todo in todo_list: 
                #immo_search_url = f'https://www.immobilienscout24.de/Suche/de/{state}/{city}/{todo}?pagenumber=1'
                immo_search_url = f'https://www.immobilienscout24.de/Suche/de/bayern/{city}/wohnung-kaufen?pagenumber=1'
                yield scrapy.Request(url=immo_search_url, callback=self.discover_product_urls, meta={'city': city, 'pagenumber':1})
    
    
    def discover_urls(self, response):
        page = response.meta['pagenumber']
        city = response.meta['city'] 
        
        if page == 1:
            available_pages = response.xpath(
                '//*[contains(@class, "p-items")]/a/text()'
            ).getall()
            last_page = available_pages[-1]     
            for page_num in range(2, int(last_page)):
                 immo_search_url = f'https://www.immobilienscout24.de/Suche/de/bayern/{city}/wohnung-kaufen?pagenumber={page_num}'
                 yield scrapy.Request(url=immo_search_url, callback=self.discover_product_urls, meta={'city': city, 'pagenumber': page_num})
    
    def parse_property(self, response): 
        script_tag  = re.findall(r'IS24\."resultList"=(\{.+?\});', response.text)
        if script_tag is not None:
            json_blob = json.loads(script_tag[0])
            
            for result in json_blob["searchResponseModel"]["resultlist.resultlist"]["resultlistEntries"][0]["resultlistEntry"]:

                    item = PropscraperItem()

                    data = result["resultlist.realEstate"]

                    print(data)

                    item['immo_id'] = data['@id']
                    item['url'] = response.urljoin("/expose/" + str(data['@id']))
                    item['title'] = data['title']
                    address = data['address']
                    try:
                        item['address'] = address['street'] + " " + address['houseNumber']
                    except:
                        item['address'] = None    
                    item['city'] = address['city']
                    item['zip_code'] = address['postcode']
                    item['district'] = address['quarter']

                    item["price"] = data["price"]["value"]
                    item["sqm"] = data["livingSpace"]
                    item["rooms"] = data["numberOfRooms"]
                    item["realtor"] = data["realtorCompanyName"]
                    try: 
                        item["realtor"] = data["realtorCompanyName"]
                    except:
                        item["realtor"] = None

                    
                    if "builtInKitchen" in data:
                        item["kitchen"] = data["builtInKitchen"]
                    if "balcony" in data:
                        item["balcony"] = data["balcony"]
                    if "garden" in data:
                        item["garden"] = data["garden"]
                    if "privateOffer" in data:
                        item["private"] = data["privateOffer"]
                 
                    if "cellar" in data:
                        item["cellar"] = data["cellar"]       

                    try:
                        contact = data['contactDetails']
                        item['contact_name'] = contact['firstname'] + " " + contact["lastname"]
                    except:
                        item['contact_name'] = None

                 

        
               
                    yield item
