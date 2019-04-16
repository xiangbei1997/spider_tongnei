# -*- coding: utf-8 -*-
import scrapy
import redis
from scrapy import Selector
from scrapy.http import Request
import time
import random
import json
import re



class ShanxiJianzhuImformationSpider(scrapy.Spider):
    name = 'another_into_guizhou'

    def start_requests(self):
        pool = redis.ConnectionPool(host='106.12.112.205', password='tongna888')
        self.r = redis.Redis(connection_pool=pool)
        self.url = 'http://jzjg.gzjs.gov.cn:8088/gzzhxt/SYGS/SYGSGL/SWRQQYGSlist_new.aspx'
        self.index = 1
        self.x = 1
        self.flag = True
        self.data = {}
        self.data['area'] = '贵州省'
        self.token = 'LnHRF8R1jmqOLFnnK048DcokeilQRDS2'
        self.data['companyArea'] = ''
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
        post_forama_data['ctl00$ContentMain$HidPageCount'] = '768'
        post_forama_data['ctl00$ContentMain$HidColnumID'] = '0'
        post_forama_data['ctl00$ContentMain$HidIndexPage'] = str(self.index)

        ul = Selector(response=response).xpath('//ul[@style="list-style: none; line-height: 30px; h'
                                                   'eight: 30px; width: 100%; border-bottom: dotted 1px #6bc1fa;"]')

        for t in ul:
            company_name = t.xpath('./li/a/@onclick').extract_first()
            re_url = 'ShowWin\(\'(.*)\',\'(.*)\',\'v\'\);return false;'
            content = re.findall(re_url, company_name)
            url = 'http://jzjg.gzjs.gov.cn:8088/gzzhxt/SysWebCenter/WebQYSB/Web_GSDWInfo_New.aspx?opType=v&GUID=%s&CorpCode=%s' %(content[0][0], content[0][1])
            print(url)
            # yield scrapy.Request(url=url)

        # self.index = self.index + 1
        # if not self.index == 2489:
        #     yield scrapy.FormRequest(url=self.url,
        #                              formdata=post_forama_data,
        #                              callback=self.parse, dont_filter=True)

    def zz(self, response):
        not_company_code = json.loads(response.text)['code']
        not_search_company_name = response.meta['company_name']
        self.r.sadd('all_company_name', not_search_company_name)
        print(response.text)
        if not_company_code == -102:
            self.r.sadd('title_name1', not_search_company_name)
            self.r.sadd('title_name3', not_search_company_name)
            print(not_search_company_name, '没找到的企业')
        else:
            print(not_search_company_name, '找到的企业')




