import scrapy


class shopSpider(scrapy.Spider):
    name = "shop_list"
    start_urls= ["https://www.honeys.co.jp/shop-result/" + str(i) for i in range(1,48)]
    
    
    def parse(self, response):
        data = response.xpath('////div/div[4]/div/div/div[2]/div/div[@class="shop_ close_0"]/div')
        for i in range(1,int(len(data)/8)+1):
            try:
                yield{
                    'name':data[8*(i-1)].xpath('text()').get(),
                    'address':data[8*(i-1)+1].xpath('text()').get(),
                    'tel':data[8*(i-1)+2].xpath('text()').get(),                                
                    'shop_code':data[8*(i-1)+5].xpath('text()').get(),                                
                }
            except:
                yield{
                    'name':'error',
                    'address':'error',
                    'tel':'error',                                
                    'shop_code':'error',                                
                }
                
        
            
