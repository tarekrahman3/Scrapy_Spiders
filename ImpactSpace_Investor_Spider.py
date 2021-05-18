import scrapy
import csv

BOT_NAME = 'ImpactSpace'
SPIDER_MODULES = ['ImpactSpace.spiders']
NEWSPIDER_MODULE = 'ImpactSpace.spiders'
DEFAULT_REQUEST_HEADERS = {
                            'authority': 'impactspace.com',
                            'method': 'GET',
                            'scheme': 'https',
                            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                            'accept-language': 'en-US,en;q=0.9,bn;q=0.8,ar;q=0.7',
                            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Mobile Safari/537.36'
                        }
ROBOTSTXT_OBEY = True
COOKIES_ENABLED = False
DOWNLOAD_DELAY = 1
CONCURRENT_REQUESTS = 100
CONCURRENT_REQUESTS_PER_DOMAIN = 70
CONCURRENT_REQUESTS_PER_IP = 70

urls = []
with open('imports.csv') as csv_file:
    reader = csv.DictReader(csv_file)
    [urls.append(row['links']) for row in reader]

class FinInvstrSpider(scrapy.Spider):
    name = 'impact_invstrs'
    allowed_domains = ['impactspace.com']
    start_urls = urls
    def parse(self, response):
        yield{
              'source' : response.url,
              'name' : response.xpath('//h1[@class="compName"]/text()').get(),
              'url' : response.xpath('//a[@itemprop="url"]/@href').get(),
              'investor_type' : response.xpath('//table[@class="overviewTable"]//tr[2]/td[1]/text()').get(),
              'operating_staus' : response.xpath('//table[@class="overviewTable"]//tr[2]/td[3]/text()').get()
            }
