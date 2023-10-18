# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2
class SaveToPostgresSQLPipeline: 
    def __init__(self):
        
        hostname = 'localhost'
        username = 'postgres'
        password = 'preet'
        database = 'immobilien'
        self.conn = psycopg2.connect(host = hostname, user = username, password = password, dbname = database)
        self.cur = self.conn.cursor()
        
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS immo(
            id SERIAL PRIMARY KEY,
            url VARCHAR(255),
            immo_id INTEGER,
            title TEXT,
            address VARCHAR(255),
            city TEXT,
            zip_code INTEGER,
            district TEXT,
            contact_name TEXT,
            sqm INTEGER,
            rooms INTEGER,
            kitchen TEXT,
            balcony TEXT,
            garden TEXT,
            private TEXT,
            cellar TEXT,
            price INTEGER,
            realtor TEXT
        
        )                
        """)    
      
    def process_item(self, item, spider):

        #define insert statement
        self.cur.execute(""" INSERT into immo(
            immo_id,
            url,
            title,
            address,
            city,
            zip_code,
            district,
            contact_name,
            sqm,
            rooms,
            kitchen,
            balcony,
            garden,
            private,
            cellar,
            price,
            realtor)VALUES(
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s
                )""",(
            item["immo_id"],
            item["url"],
            item["title"],
            item["address"],
            item["city"],
            item["zip_code"],
            item["district"],
            item["contact_name"],
            item["sqm"],
            item["rooms"],
            item["kitchen"],
            item["balcony"],
            item["garden"],
            item["private"],
            item["celler"],
            item["price"],
            item["realtor"]
            ))
        
        # Execute insert of data into database
        self.conn.commit()
        return item
    
    def close_spider(self, spider):

        ##Close cursor & connection to database
        self.cur.close()
        self.conn.close()
        #to save memory      