# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import json
import datetime
import redis
from lxml import etree

# class ZixinSpider(scrapy.Spider):
#     name = 'zixin'
#     # allowed_domains = ['www.zhujianpt.com/company']
#     start_urls = ['https://www.zhujianpt.com/company/0-1631-0-0-1.html']
#     # 去重
#     all_url = set()
#     # 获取建筑网信息
#     def parse(self, response):
#         """爬去建筑网所有公司名称"""
#         content = Selector(response=response).xpath('//ul[@class="company_contents"]/li')
#         for i in content:
#             name = i.xpath('./div[@class="name left"]/a[@target="_blank"]/text()').extract_first()
#             print('----', name)
#         page_url = Selector(response=response).xpath('//div[@class="pagination"]/a[re:test(@href,"company/0-1631-0-0-\d.html")]')
#         for p in page_url:
#             if not p.xpath('@href').extract_first() in self.all_url:
#                 self.all_url.add(p.xpath('@href').extract_first())
#                 url = 'https://www.zhujianpt.com' + p.xpath('@href').extract_first()
#                 yield Request(url)
#

#
# class zhujianCompany(object):
#     set_url = set()
#     def start_url(self):
#         zhujian_xingjiang_url = ['https://www.zhujianpt.com/company/0-1631-0-0-1.html']
#         self.headers = {
#             'Accept': 'application/json, text/javascript, */*; q=0.01',
#             'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; LDN-AL00 Build/HUAWEILDN-AL00; wv)'
#                           ' AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36'
#                           ' Html5Plus/1.0',
#         }
#         request = urllib.request.Request(zhujian_xingjiang_url, headers=self.headers)
#         response = urllib.request.urlopen(request).read().decode('utf-8')
#         print(response)
#
#
# z = zhujianCompany()
# z.start_url()
