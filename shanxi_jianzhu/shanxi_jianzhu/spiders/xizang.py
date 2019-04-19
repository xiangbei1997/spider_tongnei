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
    name = 'xizang'

    def start_requests(self):
        pool = redis.ConnectionPool(host='106.12.112.205', password='tongna888')
        self.r = redis.Redis(connection_pool=pool)
        self.index = 1
        self.url = 'http://111.11.196.111/aspx/corpinfo/CorpInfo.aspx?corpname=&cert=&PageIndex=1'
        self.flag = True
        self.into = 'XX'
        self.token = 'LnHRF8R1jmqOLFnnK048DcokeilQRDS2'
        self.bigurl = 'http://111.11.196.111'
        yield scrapy.Request(url=self.url, callback=self.parse)

    def parse(self, response):

        # a_href_all = Selector(response=response).xpath('//table[@class="table_box"]/tbody/tr/@onclick')
        a_href_all = Selector(response=response).xpath('//table[@class="table table-striped table-bordered"]'
                                                       '/tbody/tr/td[2]/a/@href')
        for t in a_href_all:
            a_url = t.extract()
            a_url = a_url.split('../..')[1]
            re_a = self.bigurl + a_url
            print(re_a)
            yield scrapy.Request(url=re_a, callback=self.company_information)
        if self.flag:
            for i in range(2, 261):
                if i == 260:
                    self.flag = False
                yield scrapy.Request(url='http://111.11.196.111/aspx/corpinfo/CorpInfo.aspx?corpname=&cert=&PageIndex=%s' % i,
                                         callback=self.parse)

    # def type_name(self, company_url):
    #     if company_url.startswith('http://jzjg.gzjs.gov.cn:8088/gzzhxt/SysWebCenter/WebQYSB/Web_GSDWInfo_New.aspx?'):
    #         scrapy.FormRequest(url=company_url, callback=self.type_name)
    #     print(company_url.url)

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

    def company_information(self, response):
        data = {}
        company_name = Selector(response=response).xpath('//td[@id="corpname"]/text()').extract_first()
        licenseNum = Selector(response=response).xpath('//td[@id="corpcode"]/text()').extract_first()
        contactMan = Selector(response=response).xpath('//td[@id="linkman"]/text()').extract_first()
        address = Selector(response=response).xpath('//td[@id="address"]/text()').extract_first()
        province = Selector(response=response).xpath('//td[@id="province"]/text()').extract_first()
        if province != '西藏自治区':
            data['companyArea'] = ''
            data['area'] = '西藏自治区'
        else:
            data['area'] = ''
            data['companyArea'] = '西藏自治区'

        data['companyName'] = company_name
        data['token'] = self.token
        data['contactMan'] = contactMan
        data['contactAddress'] = address
        data['contactPhone'] = ''
        if licenseNum != None:
            if len(licenseNum) != 18:
                data['licenseNum'] = ''
            else:
                data['licenseNum'] = licenseNum
        else:
            data['licenseNum'] = ''
        print(data)
        yield scrapy.Request(
            url='https://api.maotouin.com/rest/companyInfo/addCompanyRecord.htm',
            # url='http://192.168.199.188:8080/web/rest/companyInfo/addCompanyRecord.htm',
            method="POST",
            headers={'Content-Type': 'application/json'},
            body=json.dumps(data),
            callback=self.zz,
            meta={'company_name': company_name, 'data': data}
        )


