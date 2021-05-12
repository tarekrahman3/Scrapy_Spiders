import scrapy
from scrapy import Request
from urllib.parse import urljoin
import time

class JobsDirItem(scrapy.Item):
    parsed_moment = scrapy.Field()
    title = scrapy.Field()
    location = scrapy.Field()
    company = scrapy.Field()
    description = scrapy.Field()
    url = scrapy.Field()
    posted_date = scrapy.Field()
    required_education = scrapy.Field()

class CrawlSpiderSpider(scrapy.Spider):
    name = 'spider_w-nextpage'
    allowed_domains = ['biospace.com']
    start_urls = ["https://www.biospace.com/searchjobs/"]

    def parse(self, response):
       urls = [s.strip() for s in response.xpath('//h3[@class="lister__header"]/a/@href').getall()]
       for url in urls:
        request = Request(urljoin('https://www.biospace.com',url).strip(), callback=self.parse_job)
        yield request
       next_page = response.xpath('//a[@title="Next page"]/@href').get()
       if next_page != '':
            request_ = Request('https://www.biospace.com'+next_page, callback=self.parse)
            yield request_  
       else:
        pass
    def parse_job(self, response):
        title = response.xpath('//h1/text()').get()
        company = response.xpath('//dd/a/span/text()').get()
        posted_date = response.xpath('//div[contains(@class,"posted-date")]//dd[contains(@class,"grid-item three")]/span/text()').get()
        required_education = response.xpath('//div[contains(@class,"RequiredEducation")]//dd/a/text()').get()
        yield {'title':title,'url':response.url,'company':company,'posted_date':posted_date,'required_education':required_education,'parsed_moment':time.ctime()}

