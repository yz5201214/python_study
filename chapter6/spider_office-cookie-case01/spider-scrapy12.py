import scrapy,codecs
'''
第一次使用scrapy框架
scrapy的保存文件，默认是：Unicode，如果不转码，会形成乱码
scrapy runspider quotes_spider.py -o quotes.json -s FEED_EXPORT_ENCODING=utf-8
'''

class testScrapy(scrapy.Spider):
    name ='quotes'
    start_urls = [
        'http://lab.scrapyd.cn/',
    ]

    def __init__(self):
        self.file = codecs.open('scraped_data_utf8.json', 'w', encoding='utf-8')

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
             '内容': quote.css('span.text::text').extract_first(),
             '作者': quote.xpath('span/small/text()').extract_first(),
             '标签': quote.css('div.tags a::text').extract(),
        }
        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            yield scrapy.Request(next_page,self.parse)