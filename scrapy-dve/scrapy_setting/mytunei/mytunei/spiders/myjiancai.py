# -*- coding: utf-8 -*-
import scrapy
import sys
import io
from scrapy.http import Request
from  scrapy.selector import Selector,HtmlXPathSelector
from .. import items
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='uft-8')
# class ChoutiSpider(scrapy.Spider):
#     name = 'chouti'
#     allowed_domains = ['chouti.com']
#     start_urls = ['http://dig.chouti.com/']
#
#     def parse(self, response):
#         print('AAAAAA')
#         print(response.url)
#         # print(response.body)
#         content = str(response.body,encoding='utf-8')
#         print(content)
#         id = "top-band"
#
#         # class ="news-content"
#         # class ="content-list"
#         # class ="show-content color-chag"
#
#
#         # class="top-item"
#         # hxs = Selector(response=response).xpath('//div[@id="top-band"]/div[@id="top-content-news"]/div[@class="top-item"]')
#         # print(hxs)
#         # hxs = Selector(response=response).xpath('//div[@id="top-content-news"]/div[@class="top-item"]').extract()
#
#
#         # print(hxs)
#         # for a in hxs:
#         #     text = a.xpath('.//a[@class="top-content"]/text()').extract_first()
#         #     print(text.strip())
#
#         # print(content)
#         # print(response.body_os_unicode())
#
#
#         # hxs = Selector(response=response).xpath('//div[@id="content-list"]/div[@class="item"]/div[@class="news-content"]/div[@class="part1"]')
#         # for i in hxs:
#         #     print(i.xpath('.//a[@class="show-content color-chag"]/text()').extract_first())
#         # bigdiv = Selector(response=response).xpath('//div[@id="top-content-news"]/text()').extract_first()
#         # print(bigdiv)
#
#         # hxs = Selector(response=response).xpath('//div[@id="top-band"]/div[@id="top-content-news"')
#         # print(hxs)
#         # for i in hxs:
#         #     print(i)
#         # print(hxs)




class tunei(scrapy.Spider):
    name = 'tunei'
    allowed_domains = ['bmlink.com']
    start_urls = ['https://www.bmlink.com/']
    all_url = set()
    # def start_requests(self):
    #
    #     url = 'http://www.bmlink.com/'
    #
    #     for i in range(4):
    #         yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)
    def parse(self, response):
        print('AAAAA')

        # content = str(response.body, encoding='utf-8')
        # print(response.body)

        # all_gilr = Selector(response=response).xpath('//div[@class="item_t"]')
        # all_gilr = Selector(response=response).xpath('//div[re:test(@style,"display: block;")]')
        all_div_data = Selector(response=response).xpath('//div[@class="product"]/ul')
        # print(all_div_data)
        for i in all_div_data:

            all_il = i.xpath('./li')
            for j in all_il:
                information = j.xpath('./a/@href').extract_first()
                myurl = 'https:'+information
                # print(j.xpath('./a/@href').extract_first(),'已经访问')
                mytext = j.xpath('./a/span/text()').extract_first()
                myimg = j.xpath('./a/img/@src').extract_first()
                yield Request(url=myurl, callback=self.information_detailed)
                yield items.MytuneiItem(myurl=myurl,mytext=mytext,myimg=myimg)




    def information_detailed(self,response):
        head_text = Selector(response=response).xpath('//div[@class="sellinfo"]')
        head_text.xpath('./h1/text()').extract_first()
        head_text.xpath('./dl/dt/p[@class="price"]/text()').extract_first()
        head_text.xpath('./dl/dd/p[@class="price"]/text()').extract_first()
        head_text.xpath('./dl/dt/p[@class="order"]/text()').extract_first()
        head_text.xpath('./dl/dd/p[@class="order"]/text()').extract_first()
        head_text.xpath('./dl/dd/p[@class="price dy"]/text()').extract_first()
        url_wanzheng = head_text.xpath('./ul/li')
        # print(url_wanzheng)
        for u in url_wanzheng:
            u.xpath('text()').extract_first()





