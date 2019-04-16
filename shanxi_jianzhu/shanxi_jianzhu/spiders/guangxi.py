# -*- coding: utf-8 -*-
import scrapy
import redis
from scrapy import Selector
from scrapy.http import Request
import time
import random
import json



class ShanxiJianzhuImformationSpider(scrapy.Spider):
    name = 'guangxi'

    def start_requests(self):
        # pool = redis.ConnectionPool(host='106.12.112.207', password='tongna888')
        # self.r = redis.Redis(connection_pool=pool)
        self.url = 'http://dn4.gxzjt.gov.cn:1141/WebInfo/Enterprise/Enterprise.aspx'
        self.index = 1
        self.x = 1
        self.flag = True
        self.token = 'LnHRF8R1jmqOLFnnK048DcokeilQRDS2'
        self.bigurl = 'http://dn4.gxzjt.gov.cn:1141/WebInfo/Enterprise/'
        yield scrapy.Request(url=self.url, callback=self.parse)

    def parse(self, response):
        post_forama_data = {}
        __VIEWSTATE = Selector(response=response).xpath('//input[@id="__VIEWSTATE"]/@value').extract_first()
        __VIEWSTATEGENERATOR = Selector(response=response).xpath('//input[@id="__VIEWSTATEGENERATOR"]/@value').extract_first()
        __EVENTVALIDATION = Selector(response=response).xpath('//input[@id="__EVENTVALIDATION"]/@value').extract_first()
        __EVENTTARGET = 'ctl00$ctl00$ContentPlaceHolder1$List$Pager'
        post_forama_data['__VIEWSTATE'] = __VIEWSTATE
        post_forama_data['__VIEWSTATEGENERATOR'] = __VIEWSTATEGENERATOR
        post_forama_data['__EVENTVALIDATION'] = __EVENTVALIDATION
        post_forama_data['__EVENTTARGET'] = __EVENTTARGET
        a_href_all = Selector(response=response).xpath('//table[@id="ContentPlaceHolder1_List_Datagrid1"]/tr/td[2]/a/@href')
        # a_href_all = Selector(response=response).xpath('//table[@id="ContentPlaceHolder1_List_Datagrid1"]/tr/td[2]/a/text()')
        for t in a_href_all:
            tip = t.extract()
            # print(tip)
            yield scrapy.Request(url=self.bigurl+tip, callback=self.company_information)
        self.index = self.index + 1
        if not self.index == 10:
            post_forama_data['__EVENTARGUMENT'] = str(self.index)
            # self.Obtain(post_forama_data)
            yield scrapy.FormRequest(url=self.url,
                                     formdata=post_forama_data,
                                     callback=self.parse)


    def zz(self, response):
        print(response.text)

    def company_information(self, response):
        print(response.url, 'zzzzzzzzzzzzzzz')
        data = {}
        company_name = Selector(response=response).xpath('//span[@id="ContentPlaceHolder1_DanWeiName_8344"]/text()').extract_first()
        licenseNum = Selector(response=response).xpath('//span[@id="ContentPlaceHolder1_LicenceNum_8344"]/text()').extract_first()
        contactMan = Selector(response=response).xpath('//span[@id="ContentPlaceHolder1_LocalLianXiRen_8346"]/text()').extract_first()
        data['companyName'] = company_name
        data['area'] = ''
        data['companyArea'] = '广西壮族自治区'
        data['token'] = self.token
        data['contactMan'] = contactMan
        data['contactAddress'] = ''
        data['contactPhone'] = ''
        if licenseNum != None:
            if len(licenseNum) != 18:
                data['licenseNum'] = ''
            else:
                data['licenseNum'] = licenseNum
        else:
            data['licenseNum'] = ''
        print(data)
        yield Request(url='http://192.168.199.188:8080/web/rest/companyInfo/addCompanyRecord.htm',
                                    method="POST",
                                    headers={'Content-Type': 'application/json'},
                                    body=json.dumps(data),
                                    callback=self.zz
                      )
        # div_person = Selector(response=response).xpath('//div[@id="ent-into"]/div')
        # if len(div_person) == 2:
        #     data['contactMan'] = ''
        #     data['contactAddress'] = ''
        #     data['contactPhone'] = ''
        #     print('无人员注入')
        # else:
        #     address = div_person[3].xpath('./div/h5/text()').extract_first()
        #     person_name = div_person[4].xpath('./div/h5/text()').extract_first()
        #     phone_number = div_person[5].xpath('./div/h5/text()').extract_first()
        #     person_name = person_name.split()[0]
        #     address = address.split()[0]
        #     phone_number = phone_number.split()[0]
        #     data['contactMan'] = person_name
        #     data['contactAddress'] = address
        #     data['phone_number'] = phone_number
        # print(data)
        # yield Request(url='http://192.168.199.188:8080/web/rest/companyInfo/addCompanyRecord.htm',
        #                             method="POST",
        #                             headers={'Content-Type': 'application/json'},
        #                             body=json.dumps(data),
        #                             callback=self.zz
        #               )


