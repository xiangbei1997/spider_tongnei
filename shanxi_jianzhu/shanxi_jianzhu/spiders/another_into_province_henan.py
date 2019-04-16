# -*- coding: utf-8 -*-
import scrapy
import redis
from scrapy import Selector
from scrapy.http import Request
import time
import random
import json

class ShanxiJianzhuImformationSpider(scrapy.Spider):
    name = 'another_into_province_henan'

    def start_requests(self):
        pool = redis.ConnectionPool(host='106.12.112.205', password='tongna888')
        self.r = redis.Redis(connection_pool=pool)
        self.url = 'http://hngcjs.hnjs.gov.cn/SiKuWeb/WSRY_List.aspx'
        # self.zz_url = 'http://hngcjs.hnjs.gov.cn/SiKuWeb/WSRY_List.aspx'
        self.index = 0
        self.flag = True
        self.token = 'LnHRF8R1jmqOLFnnK048DcokeilQRDS2'
        self.data = {}
        self.data['area'] = '河南省'
        self.data['companyArea'] = ''
        self.data['contactMan'] = ''
        self.data['contactPhone'] = ''
        self.data['contactAddress'] = ''
        self.data['token'] = self.token
        self.bigurl = 'http://hngcjs.hnjs.gov.cn/SiKuWeb/'
        yield scrapy.Request(url=self.url, callback=self.parse)

    def parse(self, response):
        psot_forma_data = {}
        __VIEWSTATE  = Selector(response=response).xpath('//input[@id="__VIEWSTATE"]/@value').extract_first()
        __VIEWSTATEGENERATOR = Selector(response=response).xpath('//input[@id="__VIEWSTATEGENERATOR"]/@value').extract_first()
        __EVENTVALIDATION = Selector(response=response).xpath('//input[@id="__EVENTVALIDATION"]/@value').extract_first()
        psot_forma_data['__VIEWSTATE'] = __VIEWSTATE
        psot_forma_data['__VIEWSTATEGENERATOR'] = __VIEWSTATEGENERATOR
        psot_forma_data['__EVENTVALIDATION'] = __EVENTVALIDATION
        psot_forma_data['__EVENTTARGET'] = 'AspNetPager2'
        self.index = self.index + 1
        psot_forma_data['__EVENTARGUMENT'] = str(self.index)
        print(psot_forma_data, 'zzzzzzzzzzzzzzzz')
        tr = Selector(response=response).xpath('//a[@target="_blank"]/@href')
        print(len(tr))
        for t in tr:
            company_url = t.extract()
            print(company_url)
            print(self.bigurl + company_url)
            # print(self.bigurl + company_url)
            yield scrapy.Request(url=self.bigurl + company_url, callback=self.company_information)
        if not self.index == 180:
            yield scrapy.FormRequest(url='http://hngcjs.hnjs.gov.cn/SiKuWeb/WSRY_List.aspx',
                                     formdata=psot_forma_data,
                                     callback=self.parse)
        # del tr[0]
        # for t in tr:
        #     td = t.xpath('./td')
        #     companyName = td[1].xpath('./a/text()').extract_first()
        #     print(companyName)
        #     licenseNum = td[2].xpath('text()').extract_first()
        #     print(licenseNum)
        #     contactMan = td[3].xpath('text()').extract_first()
        #     area = td[4].xpath('text()').extract_first()
        #     data = {}
        #     data['companyName'] = companyName
        #     data['licenseNum'] = licenseNum
        #     data['contactMan'] = contactMan
        #     data['area'] = area
        #     print(data)
        # self.index = self.index + 1
        # psot_forma_data['__EVENTARGUMENT'] = str(self.index)
        # if not self.index == 1032:
        #     return scrapy.FormRequest(url='self.zz_url',
        #                               formdata=psot_forma_data,
        #                               callback=self.parse)
    def company_information(self, response):
        company_name = Selector(response=response).xpath('//span[@id="ctl00_ContentPlaceHolder1_FormView1_Label10"]/text()').extract_first()
        number = Selector(response=response).xpath('//span[@id="ctl00_ContentPlaceHolder1_FormView1_Label3"]/text()').extract_first()
        person = Selector(response=response).xpath('//span[@id="ctl00_ContentPlaceHolder1_FormView1_Label5"]/text()').extract_first()
        company_name = company_name.split()[0]
        self.data['companyName'] = company_name
        if person != None:
            person = person.split()[0]
            print(person)
            self.data['contactMan'] = person
        else:
            self.data['contactMan'] = ''
        if number != None:
            number = number.split()[0]
            print(number)
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
            meta={'company_name': company_name}
        )

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