import scrapy
import csv
urls = []
with open('imports.csv') as csv_file:
    reader = csv.DictReader(csv_file)
    [urls.append(row['links']) for row in reader]


class GetDetailsSpider(scrapy.Spider):
    name = 'get_details'
    allowed_domains = ['a2zinc.net']
    start_urls = urls

    def parse(self, response):
        yield{
            'source' : response.url,
            'name' : response.xpath('//h1/text()').get(),
            'domain' : response.xpath('//a[@id="BoothContactUrl"]/text()').get(),
            'address': response.xpath('//span[@class="BoothContactAdd1"]/text()').get(),
            'area' : response.xpath('//span[@class="BoothContactCity"]/text()').get(),
            'country' :response.xpath('//span[@class="BoothContactCountry"]/text()').get(),
            'phone' : response.xpath('//span[@class="BoothContactPhone"]/text()').get()
            }
