import scrapy
import pandas as pd
import time
import os
import random
loc = ['Mountain', 'Ranch', 'Cub', 'Snow', 'Vice', 'Empire', 'Precedent', 'Dogg', 'Cobain', 'Expo 67', 'Comfort Zone', 'The 6', 'Granville', 'Vansterdam', 'Seine', 'Castle', 'Canal', 'Red Light', 'Fjord', 'No Vampires', 'Alphorn', 'Crumpets', 'Custard', 'Ataturk', 'Victoria',]
urls =pd.read_csv('import.csv').links.tolist()

class ContactsSpider(scrapy.Spider):
    name = 'contacts'
    allowed_domains = ['allbiz.com']
    start_urls = urls

    def parse(self, response):
        if response.request.url=='https://www.allbiz.com/sorry':
            time.sleep(20)
            os.system(f"windscribe connect {loc[random.randrange(len(loc))]}")
        yield{
        'source':response.request.url,
        'contact_person':response.xpath('//p[@class="detailed-header"]/b/text()').get(),
        'title':response.xpath('//p[@class="detailed-header"]/following-sibling::p/b[contains(text(),"Title")]/../text()').get(),
        'phone':response.xpath('//i[@class="contact-icon fa fa-phone-square"]/../../a/text()').get(),
        'website':response.xpath('//i[@class="contact-icon fa fa-globe"]/../a/text()').get(),
        'email':response.xpath('//i[@class="contact-icon fa fa-envelope-square"]/../a/text()').get(),
        'address':response.xpath('//address/text()').get()
        }
