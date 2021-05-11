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
    name = 'crawl_spider'
    allowed_domains = ['biospace.com']
    start_urls = ["https://www.biospace.com/searchjobs/?countrycode=US&Page=" + str(i) for i in range(303)]

    def parse(self, response):
       urls = [s.strip() for s in response.xpath('//h3[@class="lister__header"]/a/@href').getall()]
       for url in urls:
        request = Request(urljoin('https://www.biospace.com',url).strip(), callback=self.each_job)
        yield request
       
       next_page_href = response.xpath('//a[@title="Next page"]/@href').get()
       if next_page_href:
        yield scrapy.Request(response.urljoin(next_page_href), callback=self.parse)

    def each_job(self, response):
        yield {
            'parsed_moment':time.ctime(),
            'title':response.xpath('//h1/text()').get(),
            'url':response.url,
            'company':response.xpath('//dd/a/span/text()').get(),
            'posted_date':response.xpath('//div[contains(@class,"posted-date")]//dd[contains(@class,"grid-item three")]/span/text()').get(),
            'required_education': response.xpath('//div[contains(@class,"RequiredEducation")]//dd/a/text()').get()
            }
