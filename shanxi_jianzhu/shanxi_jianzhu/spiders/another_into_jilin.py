# -*- coding: utf-8 -*-
import scrapy
import redis
from scrapy import Selector
import time
import json
class ShanxiJianzhuImformationSpider(scrapy.Spider):
    name = 'another_into_jilin'

    def start_requests(self):
        pool = redis.ConnectionPool(host='106.12.112.205', password='tongna888')
        self.r = redis.Redis(connection_pool=pool)
        now_time = time.time() * 1000 - 1000000
        self.index = 1
        self.data = {}
        self.data['area'] = '吉林省'
        self.data['companyArea'] = ''
        self.token = 'LnHRF8R1jmqOLFnnK048DcokeilQRDS2'
        self.data['token'] = self.token
        self.bigurl = 'http://cx.jlsjsxxw.com/'
        self.url = 'http://cx.jlsjsxxw.com/handle/NewHandler.ashx?method=SwCorpData' \
                   '&CorpName=' \
                   '&AptitudeNum=' \
                   '&TradeID=' \
                   '&BoundID=' \
                   '&LevelID=' \
                   '&ProvinceNum=' \
                   '&nPageIndex=%s' \
                   '&nPageCount=126' \
                   '&nPageRowsCount=2516' \
                   '&nPageSize=%s' \
                   '&_=%s' % (1, 20, now_time)
        self.province_flag = True
        self.province = 1
        yield scrapy.Request(url=self.url, callback=self.parse)

    def parse(self, response):
        zz = Selector(response=response).xpath('//tr/td[2]/a/@href')
        print(len(zz))
        for z in zz:
            company_name = z.extract()
            company_name = company_name.split(r'\"')[1]
            url = company_name.split('..')[1]
            print(url)
            print(self.bigurl + url)

            yield scrapy.Request(url=self.bigurl + url, callback=self.company_information)
        self.index = self.index + 1
        if self.index != 127:
                print('当前第%s多少页' % self.index)
                now_time = time.time() * 1000 - 1000000
                yield scrapy.Request(url='http://cx.jlsjsxxw.com/handle/NewHandler.ashx?method=SwCorpData&CorpName=&AptitudeNum=&TradeID=&BoundID=&LevelID=&ProvinceNum=&nPageIndex=%s&nPageCount=126&nPageRowsCount=2516&nPageSize=20&_=%s' % (self.index, now_time), callback=self.parse)

    def company_information(self, response):
        company_name = Selector(response=response).xpath('//td[@class="name_level3"]')[0].xpath('text()').extract_first()
        number = Selector(response=response).xpath('//td[@id="Td3"]/text()').extract_first()
        person = Selector(response=response).xpath('//td[@id="EconType"]/text()').extract_first()
        address = Selector(response=response).xpath('//td[@id="LicenseNum"]/text()').extract_first()
        phone = Selector(response=response).xpath('//td[@id="RegPrin"]/text()').extract_first()
        company_name = company_name.split()[0]
        if phone == None:
            self.data['contactPhone'] = ''
        else:
            phone = phone.split()
            phone = phone[0]
            if phone == '/':
                self.data['contactPhone'] = ''
            else:
                self.data['contactPhone'] = phone
        if person == None:
            self.data['contactMan'] = ''
        else:
            person = person.split()
            person = person[0]
            self.data['contactMan'] = person
        if address == None:
            self.data['contactAddress'] = ''
        else:
            address = address.split()
            address = address[0]
            self.data['contactAddress'] = address
        if number != None:
            number = number.split()
            number = number[0]
            if len(number) != 18:
                self.data['licenseNum'] = ''
            else:
                self.data['licenseNum'] = number
        else:
            self.data['licenseNum'] = ''
        self.data['companyName'] = company_name
        print(self.data)
        yield scrapy.Request(
            url='https://api.maotouin.com/rest/companyInfo/addCompanyRecord.htm',
            # url='http://192.168.199.188:8080/web/rest/companyInfo/addCompanyRecord.htm',
            method="POST",
            headers={'Content-Type': 'application/json'},
            body=json.dumps(self.data),
            callback=self.zz,
            meta={'company_name': company_name,'data':self.data}
        )

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
