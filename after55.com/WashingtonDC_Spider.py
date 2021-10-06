# -*- coding: utf-8 -*-
import scrapy
import scrapy
from scrapy import Request

class WashingtonDcSpider(scrapy.Spider):
    name = 'Washington_DC'
    allowed_domains = ['after55.com']
    start_urls = ['https://www.after55.com/dc/washington']

    def parse(self, response):
        urls = response.xpath("//span[@class='org']/a/@href").getall()
        for url in urls:
            print(url)
            request = Request(url, callback = self.parse_appointments)
            yield request
        
        next_page = response.xpath('//div[contains(@class,"serpPagination")]//a[text()=" NEXT "]/@href').get()
        if next_page != '':
            request_ = Request(next_page, callback = self.parse)
            yield request_
        else:
            pass
    
    def parse_appointments(self, response):
        name = response.xpath('//h1/text()').get()
        street_address = response.xpath('//span[@class="street-address"]/text()').get()
        city = response.xpath('//span[@class="locality"]/text()').get()
        state = response.xpath('//span[@class="region"]/text()').get()
        zip_code = response.xpath('//span[@class="postal-code"]/text()').get()
        phone = response.xpath('//span[@class="phone_block"]/a[@id="phonebutton"]/text()').get()
        yield {
        'source':response.url,
        'name':name,
        'street_address':street_address,
        'city':city,
        'state':state,
        'zip_code':zip_code,
        'phone':phone
        }

