import scrapy
from scrapy import Request
from urllib.parse import urljoin
import time

DEFAULT_REQUEST_HEADERS = {
    'authority': 'www.guidestar.org',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,bn;q=0.8,ar;q=0.7',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Mobile Safari/537.36'
    }
class GuideorgNonprofitsSpider(scrapy.Spider):
    name = 'guideorg_nonprofits'
    allowed_domains = ['guidestar.org']
    start_urls = [f"https://www.guidestar.org/nonprofit-directory/education-research/libraries/{str(i)}.aspx" for i in range(69)]

    def parse(self, response):
        hrefs = ['https://www.guidestar.org' + href for href in response.xpath('//a[contains(@href,"profile")]/@href').getall()]
        for url in range(len(hrefs)-1):
            request = Request(hrefs[url], callback=self.parse_each)
            yield request
       
       
    def parse_each(self, response): 
        yield {
            'source': response.url,
            'org_title': (response.xpath('//h1[contains(@class,"profile-org-name")]/text()').get()).strip(),
            'org_aka': response.xpath('//div[@class="description pt-3"]/span[1]').get(),
            'org_website': response.xpath('//div[@class="description pt-3"]//a[@href]/@href').get(),
            'org_city': response.xpath('//div[@class="description pt-3"]/span[2]/text()').get(),
            #'ruling_year': response.xpath().get(),
            'ein': response.xpath('//div[@class="col-lg-2"][2]/section[1]/p[2]/text()').get(),
            #'main_address': response.xpath().get(),
            'ntee_code': response.xpath('//div[@class="col-lg-2"][2]/section[2]/p[2]/text()').get()
            #'mission': response.xpath().get(),
            #'programs': response.xpath().get()
        }
