import scrapy
import pandas as pd

urls = pd.read_csv('import.csv').links.tolist()

class UniversitySpider(scrapy.Spider):
    name = 'university'
    allowed_domains = ['wikipedia.org']
    start_urls = urls

    def parse(self, response):
        ch = response.xpath('//th[a[text()="Chairman"]]/following-sibling::td/a/text()').get()
        chairman = response.xpath('//th[a[text()="Chairman"]]/following-sibling::td/text()').get() if ch==None else ch
        pr = response.xpath('//th[a[text()="President"]]/following-sibling::td/a/text()').get()
        president = response.xpath('//th[a[text()="President"]]/following-sibling::td/text()').get() if pr==None else pr
        c = response.xpath('//th[a[text()="Chancellor"]]/following-sibling::td/a/text()').get()
        chancellor = response.xpath('//th[a[text()="Chancellor"]]/following-sibling::td/text()').get() if c==None else c
        vc = response.xpath('//th[span/a[text()="Vice-Chancellor"]]/following-sibling::td/a/text()').get()
        Vice_Chancellor =response.xpath('//th[span/a[text()="Vice-Chancellor"]]/following-sibling::td/text()').get() if vc==None else vc
        d = response.xpath('//th[a[text()="Dean"]]/following-sibling::td/a/text()').get()
        dean = response.xpath('//th[a[text()="Dean"]]/following-sibling::td/text()').get() if d==None else d
        pv = response.xpath('//th[a[text()="Provost"]]/following-sibling::td/a/text()').get()
        provost = response.xpath('//th[a[text()="Provost"]]/following-sibling::td/text()').get() if pv==None else pv
        pp = response.xpath('//th[text()="Principal"]/following-sibling::td/text()').get()
        principal = response.xpath('//th[text()="Principal"]/following-sibling::td/a/text()').get() if pp==None else pp
        s = response.xpath('//th[a[text()="Superintendent"]]/following-sibling::td/a/text()').get()
        superintendent = response.xpath('//th[text()="Superintendent"]/following-sibling::td/text()').get() if s==None else s
        co = response.xpath('//th[text()="Superintendent"]/following-sibling::td/a/text()').get()
        commandant = response.xpath('//th[a[text()="Commandant"]]/following-sibling::td/text()').get() if co==None else co
        yield {
            'source':response.request.url,
            'title': response.xpath('//h1[@id="firstHeading"]/text()').get(),
            'website': response.xpath('//th[text()="Website"]/following-sibling::td//a/@href').get(),
            'location': response.xpath('//th[text()="Location"]/following-sibling::td/text()').get(),
            'chairman' : chairman,
            'chancellor': chancellor,
            'vice-vhancellor': Vice_Chancellor,
            'president' : president,
            'provost' : provost,
            'dean':dean,
            'principal': principal,
            'superintendent': superintendent,
            'commandant' : commandant,
        }
