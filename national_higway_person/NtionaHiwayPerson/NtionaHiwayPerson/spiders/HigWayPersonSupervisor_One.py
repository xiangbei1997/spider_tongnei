# -*- coding: utf-8 -*-
import scrapy
import redis
import json


class HigWayPersonSpider(scrapy.Spider):
    name = 'HigWayPersonSupervisor'

    def __init__(self, name=None, **kwargs):
        super().__init__(name=None, **kwargs)
        self.url = 'http://glxy.mot.gov.cn/person/getPersonList.do'
        pool = redis.ConnectionPool(host='106.12.112.205', password='tongna888')
        self.r = redis.Redis(connection_pool=pool)
        self.token = 'LnHRF8R1jmqOLFnnK048DcokeilQRDS2'
        self.start_formats = {'page': '1', 'rows': '15', 'type': '1'}

    def start_requests(self):
        yield scrapy.FormRequest(url=self.url,
                                 callback=self.parse,
                                 formdata=self.start_formats,
                                 )

    def parse(self, response):
        highways_data = {}
        data = json.loads(response.text)
        max_page = data['pageObj']['maxPage']
        print('当前页共%s---共有-%s页' % (len(data['rows']), max_page))
        for p in data['rows']:
            highways_data['companyName'] = p['company']
            highways_data['licenseNum'] = ''
            highways_data['birthDate'] = p['birthDate']
            highways_data['idType'] = p['idType']
            highways_data['idCard'] = p['idCard']
            highways_data['majorStartDate'] = p['majorStartDate']
            highways_data['name'] = p['name']
            highways_data['sex'] = p['sex']
            highways_data['status'] = p['status']
            highways_data['topCollege'] = p['topCollege']
            highways_data['topEducation'] = p['topEducation']
            highways_data['topMajor'] = p['topMajor']
            highways_data['address'] = p['address']
            highways_data['nation'] = p['nation']
            highways_data['engagedInSpecialty'] = p['engagedInSpecialty']
            highways_data['engagedYears'] = p['engagedyears']
            highways_data['companyYear'] = p['companyYear']
            highways_data['technicalTitle'] = p['technicalTitle']
            highways_data['professionalTitle'] = p['professionalTitle']
            if p['jobResume'] == '':
                highways_data['jobResume'] = ''
            else:
                highways_data['jobResume'] = p['jobResume'].split()[0]
            highways_data['tokenKey'] = self.token
            print(highways_data)
            yield scrapy.FormRequest(url='http://192.168.199.188:8080/web/rest/companyInfo/addRoadCompanyEngineer.htm',
                                     formdata=highways_data,
                                     callback=self.zz)
        page = int(self.start_formats['page'])
        max_page = data['pageObj']['maxPage']
        page += 1
        if page != (max_page + 1):
            self.start_formats['page'] = str(page)
            yield scrapy.FormRequest(url=response.url,
                                     formdata=self.start_formats,
                                     callback=self.parse,
                                     )

    def zz(self, response):
        print(response.text)
