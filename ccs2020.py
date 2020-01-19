# -*- coding: utf-8 -*-
import scrapy
import csv


class CcsSpider(scrapy.Spider):
    name = 'ccs'
    # apiUrl = 'https://blockchain.com/eth/address/{}'
    apiUrl = 'https://blockchair.com/ethereum/address/{}'
    start = []
    
    with open('keys.csv','rt') as f:
        data = csv.reader(f)
        for url in data:
            addr = apiUrl.format(url[0])
            start.append(addr)
    
    start_urls = start

# #########################transactionCount##########################
    def parse(self, response):
        a = response.css('ul.block__ul')
        yield {
            # 'url': response.url,
            'countTX': a.css('li.block__item span::text')[13].get()
        }

# #########################inCall,outCall##########################
    # def parse(self, response):
    #     a = response.css('ul.block__ul')
    #     yield {
    #         'inCall': a.css('span a::text')[0].get() #inCall
    #         # 'outCall': a.css('span a::text')[1].get() #outCall
    #     }

# #########################inEther,outEther##########################
    # def parse(self, response):
    #     a = response.css('div.grey')
    #     b = a.css('span::text')[0].get()
    #     c = a.css('span::text')[1].get()
    #     d = b+c
    #     yield {
    #         'inEther': d
    #     }

    # def parse(self, response):
    #     a = response.css('div.grey')
    #     b = a.css('span::text')[5].get()
    #     c = a.css('span::text')[6].get()
    #     d = b + c
    #     yield {
    #         'outEther': d
    #     }
    
# #########################feeEther##########################
    # def parse(self, response):
    #     a = response.css('li.block__item')
    #     b = a.css('span.not span::text').get()
    #     c = a.css('span.not span.grey::text').get()
    #     d = b + c
    #     yield {
    #         'feeEther': d
    #     }

##################################################################
    # def parse(self, response):
    #     a = response.css('div.sc-8sty72-0')
    #     yield {
    #         'countTX': a.css('span.sc-1ryi78w-0::text')[5].get()
    #     }
