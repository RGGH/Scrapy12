# scraped cookpad.com/uk

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy import Request

class cookpad(scrapy.Spider):

    name = 'cookpad'
    
    start_urls = ['https://cookpad.com/uk']

    headers = { 'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Host': 'https://cookpad.com/uk',
            'Referer': 'https://cookpad.com/uk',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'}

    
    def parse(self, response):
    
        listings = response.xpath('//*[@class="card border-none mt-3"]')
        for card in listings:
            link = card.xpath(".//a[@class='h-full flex bg-black-transparent rounded-t overflow-hidden']/@href").get()
            print(link)
            # yield to link (parse_details)
            
        if response.xpath("//a/@rel='next\'").get() == "1":
            print("GET Next Page")
            next_page = response.xpath('//a[@rel="next"]/@href').get()
            yield response.follow(url=next_page,callback=self.parse)
        

    def parse_details(self, response):
        pass      
        
 
 
 
 
 # main driver 
if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(cookpad)
    process.start()
