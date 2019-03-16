# -*- coding: utf-8 -*-
import scrapy
from scrapy import  Selector
from scrapy.http import Request,Response

import time
import json
class AllXinliangSpider(scrapy.Spider):
    name = 'all_xinliang'
    # allowed_domains = ['xinliang.com']
    # start_urls = ['http://jzsc.mohurd.gov.cn/dataservice/query/comp/list']

    def start_requests(self):
        self.big_url = 'http://jzsc.mohurd.gov.cn'
        # self.url = 'http://jzsc.mohurd.gov.cn/dataservice/query/comp/'
        self.url = 'http://jzsc.mohurd.gov.cn/dataservice/query/comp/list'
        # http: // jzsc.mohurd.gov.cn / dataservice / query / comp / caDetailList /
        self.corporate_name = '汶上县建筑设计院有限公司'
        self.time = None
        # return [scrapy.FormRequest(self.url,
        #                        formdata={'qy_type':"",'apt_scope':"",'apt_code':"",'qy_name':self.corporate_name,
        #                                  'qy_code':"",'apt_certno':"",'qy_fr_name':"",'qy_gljg':"",'qy_reg_addr':"",'qy_region':""},
        #                        callback=self.parse)]
        return [scrapy.FormRequest(self.url,
                                   formdata={'qy_name': self.corporate_name},
                                   callback=self.parse)]
    def parse(self, response):
        # self.time = (time.time() * 1000)
        corporate_url = Selector(response=response).xpath('//td[@class="text-left primary"]/a/@href').extract_first()
        print(corporate_url)
        # ''.split('/')[:-1]
        # self.number = corporate_url.split('/')[-1:][0]

        url = self.big_url + corporate_url
        # print("AAAA")
        return Request(url=url,callback=self.detailed_information)


    def detailed_information(self, response):
        # self.time = (time.time() * 1000)
        self.company_dir = {}
        # print('AAA')
        self.company_information = Selector(response=response).xpath('//div[@class="user_info spmtop"]/b/text()').extract_first()
        self.company_dir[self.company_information] = {}
        table_information = Selector(response=response).xpath('//table[@class="pro_table_box datas_table"]/tbody/tr')
        # print(table_information)
        for t in table_information:
            # print(t.xpath('./td/@data-header').extract_first(), '表头')
            # print(t.xpath('./td/text()').extract_first(), '内容')
            table_hand = t.xpath('./td/@data-header').extract_first()
            table_body = t.xpath('./td/text()').extract_first()
            self.company_dir[self.company_information][table_hand] = table_body
        enterprise_qualification = Selector(response=response).xpath('//a[@id="apt_tab"]/span/text()').extract_first()
        enterprise_url = Selector(response=response).xpath('//ul[@class="tinyTab datas_tabs"]/li')
        for e in enterprise_url:
            url = self.big_url + e.xpath('./a/@data-url').extract_first()
            self.span = e.xpath('./a/span/text()').extract_first()

            self.company_dir[self.company_information][self.span] = {}
            yield Request(url=url, callback=self.zz)
            # text = json.dumps(text)
            # text = Selector(response=text).xpath('//div')
            # print(dir(text))
            # print(text.body)
            # good = Selector(response=text).xpath('//tbody[@class="cursorDefault]"')
            # for t in good:
            #     head = t.xpath('./td/@data-header')
            #     body = t.xpath('./td/text()')
            #     company_dir[company_information][span][head] = body
            # # Selector(response=text).xpath('//tbody[@class="cursorDefault]"')
        print(self.company_dir)
        # print(enterprise_url)
    def zz(self,response):
        self.company_dir[self.company_information][self.span] = {}
        connet = Selector(response=response).xpath("//tbody/tr")
        for c in connet:
            all_td = c.xpath('./td')
            for a in all_td:
                head = a.xpath('./@data-header').extract_first()
                print(head)
                body = a.xpath('./text()').extract_first()
                print(body)
                self.company_dir[self.company_information][self.span][head] = body
        # print(table_enterprise)
        # for t in table_enterprise:
        #     print(t.xpath('./td/@data-header'),'head')
        #     print(t.xpath('./td/text()'), 'body')

        # company_dir[company_information][enterprise_qualification] = {}

        # text = Request()
        # print(text)
        # scrapy.Request(url=)
        # print(enterprise_qualification)
        # print(response)
        # table_enterprise = Selector(response=response).xpath('//div[@id = "tableContent"]/table')
        # print(table_enterprise)
        # for t in table_enterprise:
        #     print(t.xpath('./td/@data-header'),'head')
        #     print(t.xpath('./td/text()'), 'body')
        # company_dir[company_information][enterprise_qualification] = {}
