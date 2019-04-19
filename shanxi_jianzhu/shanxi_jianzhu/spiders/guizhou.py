# -*- coding: utf-8 -*-
import scrapy
import redis
from scrapy import Selector
from scrapy.http import Request
import time
import random
import json



class ShanxiJianzhuImformationSpider(scrapy.Spider):
    name = 'guizhou'

    def start_requests(self):
        pool = redis.ConnectionPool(host='106.12.112.205', password='tongna888')
        self.r = redis.Redis(connection_pool=pool)
        self.url = 'http://jzjg.gzjs.gov.cn:8088/gzzhxt/SYGS/SYGSGL/QYCX_new.aspx'
        self.index = 1
        self.x = 1
        self.flag = True
        self.data = {}
        self.data['area'] = ''
        self.token = 'LnHRF8R1jmqOLFnnK048DcokeilQRDS2'
        self.data['companyArea'] = '贵州省'
        self.data['token'] = self.token
        self.data['contactMan'] = ''
        self.data['contactAddress'] = ''
        self.data['contactPhone'] = ''
        self.bigurl = 'http://220.160.52.164:96/ConstructionInfoPublish/Pages/'
        yield scrapy.Request(url=self.url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        post_forama_data = {}
        __VIEWSTATE = Selector(response=response).xpath('//input[@id="__VIEWSTATE"]/@value').extract_first()
        __EVENTVALIDATION = Selector(response=response).xpath('//input[@id="__EVENTVALIDATION"]/@value').extract_first()
        __VIEWSTATEGENERATOR = Selector(response=response).xpath('//input[@id="__VIEWSTATEGENERATOR"]/@value').extract_first()
        post_forama_data['__VIEWSTATE'] = __VIEWSTATE
        post_forama_data['__VIEWSTATEGENERATOR'] = __VIEWSTATEGENERATOR
        post_forama_data['__EVENTVALIDATION'] = __EVENTVALIDATION
        post_forama_data['__EVENTTARGET'] = 'ctl00$ContentMain$LinkButtonNextPage'
        post_forama_data['ctl00$ContentMain$HidPageCount'] = '2488'
        post_forama_data['ctl00$ContentMain$HidColnumID'] = '0'
        post_forama_data['ctl00$ContentMain$HidIndexPage'] = str(self.index)

        ul = Selector(response=response).xpath('//ul[@style="list-style: none; line-height: 30px; h'
                                                   'eight: 30px; width: 100%; border-bottom: dotted 1px #6bc1fa;"]')

        for t in ul:
            company_name = t.xpath('./li/a/@title').extract_first()
            number = t.xpath('./li[2]/text()').extract_first()
            self.data['companyName'] = company_name
            if number != None:
                if len(number) != 18:
                    self.data['licenseNum'] = ''
                else:
                    self.data['licenseNum'] = number
            else:
                self.data['licenseNum'] = ''
            print(self.data)
            yield scrapy.Request(
                url='https://api.maotouin.com/rest/companyInfo/addCompanyRecord.htm',
                # url='http://192.168.199.188:8080/web/rest/companyInfo/addCompanyRecord.htm',
                method="POST",
                headers={'Content-Type': 'application/json'},
                body=json.dumps(self.data),
                callback=self.zz,
                meta={'company_name': company_name, 'data': self.data}
            )

        self.index = self.index + 1
        if not self.index == 2492:
            yield scrapy.FormRequest(url=self.url,
                                     formdata=post_forama_data,
                                     callback=self.parse, dont_filter=True)

    def zz(self, response):
        not_company_code = json.loads(response.text)['code']
        not_search_company_name = response.meta['company_name']
        zz_data = response.meta['data']
        self.r.sadd('all_company_name', not_search_company_name)
        print(response.text)
        data = json.dumps(zz_data, ensure_ascii=False)
        print(response.meta['data'], 'aaaaaaaaaaaaaaaaaa')
        if not_company_code == -102:
            self.r.sadd('title_name1', not_search_company_name)
            self.r.sadd('title_102', data)
            self.r.sadd('title_name3', not_search_company_name)
            print(not_search_company_name, '没找到的企业')
        else:
            print(not_search_company_name, '找到的企业')




