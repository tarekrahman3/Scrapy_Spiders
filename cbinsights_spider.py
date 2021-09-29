import scrapy
import pandas as pd

urls = pd.read_csv('import.csv').links.tolist()

class LocationSpider(scrapy.Spider):
    name = 'location'
    allowed_domains = ['cbinsights.com']
    start_urls = urls

    def parse(self, response):
        yield{
        'source':response.request.url,
        'country':response.xpath('//*[@data-test="country"]/text()').get(),
        'phone':response.xpath('//*[@data-test="phone"]/text()').get()
        }
