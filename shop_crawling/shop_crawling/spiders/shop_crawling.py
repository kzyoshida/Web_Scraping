import scrapy


class shopSpider(scrapy.Spider):
    name = "shop_list"
    start_url = ["https://www.honeys.co.jp/shop-result/01"]
    
    
    def parse(self, response):
        for products in response.xpath('////div/div[4]/div/div/div[2]/div/div[3]/div[1]/text()').get():
            yield(
                'name':products,
                # 'address':,
                # 'tel':,                                
            )
        
            
