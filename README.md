# Scrapy12

## Scrapy : cookpad.com/uk

### Infinite scroll pagination with a twist 

            if response.xpath("//a/@rel='next\'").get() == "1":
            print("GET Next Page")
            next_page = response.xpath('//a[@rel="next"]/@href').get()
            yield response.follow(url=next_page,callback=self.parse)
            
https://github.com/RGGH/Misc/blob/master/cookpad_screenshot.PNG
