# -*- coding: utf-8 -*-
import scrapy
import redis
from scrapy import Selector
from scrapy.http import Request
import json
class ShanxiJianzhuImformationSpider(scrapy.Spider):
    name = 'another_province_into_tendering'

    def start_requests(self):
        pool = redis.ConnectionPool(host='106.12.112.205', password='tongna888')
        self.r = redis.Redis(connection_pool=pool)
        self.url = 'http://js.shaanxi.gov.cn:9010/SxApp/share/WebSide/ZZCXSGList.aspx?fsid=320'
        self.whole_url = 'http://js.shaanxi.gov.cn:9010/SxApp/share/WebSide/ZZCXSGList.aspx?fsid=320'
        self.flag = True
        self.index = 1
        self.data = {}
        self.token = 'LnHRF8R1jmqOLFnnK048DcokeilQRDS2'
        self.data['licenseNum'] = ''
        self.data['contactMan'] = ''
        self.data['area'] = '陕西省'
        self.data['companyArea'] = ''
        self.data['contactAddress'] = ''
        self.data['contactPhone'] = ''
        self.data['token'] = self.token
        yield scrapy.Request(url=self.whole_url, callback=self.parse)
    def parse(self, response):
        __VIEWSTATE = Selector(response).xpath('//input[@id="__VIEWSTATE"]/@value').extract_first()
        __VIEWSTATEGENERATOR = Selector(response).xpath('//input[@id="__VIEWSTATEGENERATOR"]/@value').extract_first()
        __EVENTVALIDATION = Selector(response).xpath('//input[@id="__EVENTVALIDATION"]/@value').extract_first()
        div_under_table = Selector(response).xpath('//div[@class="ch_Grid"]/table/tr/td[2]/text()')
        print('parse', self.index)
        formdata = {}
        if __EVENTVALIDATION != None:
            formdata['__EVENTVALIDATION'] = __EVENTVALIDATION
        formdata['__VIEWSTATE'] = __VIEWSTATE
        formdata['__EVENTTARGET'] = 'Pager1'
        formdata['__EVENTARGUMENT'] = str(self.index)
        formdata['__VIEWSTATEGENERATOR'] = __VIEWSTATEGENERATOR
        print(formdata)
        for d in div_under_table:
            company_name = d.extract()
            company_name = company_name.split()[0]
            print(company_name)
            print(self.data)
            self.data['companyName'] = company_name
            yield scrapy.Request(
                url='https://api.maotouin.com/rest/companyInfo/addCompanyRecord.htm',
                # url='http://192.168.199.188:8080/web/rest/companyInfo/addCompanyRecord.htm',
                method="POST",
                headers={'Content-Type': 'application/json'},
                body=json.dumps(self.data),
                callback=self.zz,
                meta={'company_name': company_name}
            )
        self.index = self.index + 1
        if not self.index == 7:
            yield scrapy.FormRequest(url=self.url, callback=self.parse, formdata=formdata)

    def zz(self, response):
        not_company_code = json.loads(response.text)['code']
        if not_company_code == -102:
            not_search_company_name = response.meta['company_name']
            self.r.sadd('title_name1', not_search_company_name)
            self.r.sadd('title_name3', not_search_company_name)
            print(not_search_company_name, '没找到的企业')
        else:
            print(response.meta['company_name'], '找到的企业')