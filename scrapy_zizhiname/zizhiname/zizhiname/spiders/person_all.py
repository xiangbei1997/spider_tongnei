# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
from scrapy.http import Request,Response
import requests
import json
class AllXinliangSpider(scrapy.Spider):
    # 执行名称
    name = 'person_all'
    def start_requests(self):
        """爬虫起始"""
        self.token = 'uBgLy2zN88aTokllUWlyEZ2l6AK2k2dn'
        # 本公司接口
        self.tongnie = 'http://192.168.199.188:8080/web/rest/companyInfo/addCompanyEngineer.htm'
        # 起始url
        self.big_url = 'http://jzsc.mohurd.gov.cn'
        # form表单url
        self.url = 'http://jzsc.mohurd.gov.cn/dataservice/query/comp/list'
        # 提交form数据
        self.corporate_name = '浙江大成工程项目管理有限公司'
        # 访问并携带参数
        return [scrapy.FormRequest(self.url,
                                   formdata={'qy_name': self.corporate_name},
                                   callback=self.parse)]
    def parse(self, response):
        # 进入当前公司
        """选择公司"""
        corporate_url = Selector(response=response).xpath('//td[@class="text-left primary"]/a/@href').extract_first()
        # print(corporate_url)
        url = self.big_url + corporate_url
        return Request(url=url, callback=self.detailed_information)
    def detailed_information(self, response):
        """人员基本信息表"""
        url = Selector(response=response).xpath('//ul[@class="tinyTab datas_tabs"]/li[2]/a/@data-url').extract_first()
        # print(url)
        url = self.big_url + url
        return Request(url=url, callback=self.person)
    def person(self,response):
        """当前公司所有人员url"""
        tr = Selector(response=response).xpath('//tbody/tr')
        for r in tr:
            # print(r.xpath('./td/a'))
            one_person = r.xpath('./td/a/@onclick').extract_first()
            if not one_person == None:
                # person_name = r.xpath('./td/a/text()').extract_first()
                print(one_person)
                person_url = one_person.split('top.window.location.href=\'')[1]
                # print()
                person_url = person_url.split('\'')[0]
                person_url = self.big_url + person_url
                yield Request(url=person_url, callback=self.person_detailed)
    def person_detailed(self,response):
        """人员证件详细表"""

        # 需要发送的人员证件信息
        person_document = {}
        person_document['companyName '] = self.corporate_name
        # 人员名称
        person_name = Selector(response=response).xpath('//div[@class="user_info spmtop"]/b/text()').extract_first()
        person_document['name'] = person_name

        # 人员性别
        person_sex = Selector(response=response).xpath('//dd[@class="query_info_dd1"]/text()').extract_first()
        person_document['sex'] = person_sex

        # 证件类型
        document_type = Selector(response=response).xpath('//div[@class="activeTinyTabContent"]/dl/dd[2]/text()').extract_first()
        person_document['idType'] = document_type

        # 证件编号
        ducoment_number = Selector(response=response).xpath('//div[@class="activeTinyTabContent"]/dl/dd[3]/text()').extract_first()
        person_document['card'] = ducoment_number

        # 执业注册信息----传递数据
        registration_name = Selector(response=response).xpath('//ul[@class="tinyTab datas_tabs"]/li[@class="activeTinyTab"]/a/span/text()').extract_first()
        # person_document['grade'] = registration_name

        # 证件相关信息
        document_person = Selector(response=response).xpath('//div[@id="regcert_tab"]/dl')
        # print(registration_name)
        for dl in document_person:
            # 人员名称
            # person_document = {}
            dt = dl.xpath('./dt')
            dl = dl.xpath('./dd')
            dl.append(dt)
            for dd in dl:
                one_person_data = dd.xpath('./span/text()').extract_first()
                if one_person_data == '注册类别：':
                    register_type = dd.xpath('./b/text()').extract_first()
                    person_document['grade'] = register_type

                elif one_person_data == '注册专业：':
                    register_major = dd.xpath('text()').extract_first()
                    person_document['major'] = register_major

                elif one_person_data == '证书编号：':
                    certificate_number = dd.xpath('text()').extract_first()
                    person_document['num'] = certificate_number

                elif one_person_data == '执业印章号：':
                    practice_seal_number = dd.xpath('text()').extract_first()
                    person_document['sealNum'] = practice_seal_number
                elif one_person_data == '有效期：':
                    term_of_validity = dd.xpath('text()').extract_first()
                    # ''.split('日')[]
                    term_of_validity = term_of_validity.replace('年', '-')
                    term_of_validity = term_of_validity.replace('月', '-')
                    term_of_validity = term_of_validity.split('日')[0]
                    person_document['validTime'] = term_of_validity

                elif one_person_data == '注册单位：':
                    registered_unit = dd.xpath('./a/text()').extract_first()
                    registered_unit = registered_unit.split()[0]
                    # print('注册单位', registered_unit)
                    person_document['companyName'] = registered_unit
                # 证件信息发送一条
            # print(person_document)
            person_document['token'] = self.token
            yield Request(url=self.tongnie, method="POST", body=json.dumps(person_document), headers={'Content-Type': 'application/json'},callback=self.zz)
        # another_page = Selector(response=response).xpath('//div[@class="clearfix"]')
        # print(another_page)
        # print(another_page)
        # my_url = set()
        # if not another_page == []:
        #     for a in another_page:
        #         page_url = a.xpath('./@dt').extract_first()
        #         if not page_url in my_url:
        #             if not page_url == '1':
        #                 my_url.add(page_url)
        #                 print('aaaaaaaaaaaaaaaaaa')
        #                 print(page_url)
        #                 yield scrapy.FormRequest(response.url, formdata={'pg': page_url}, callback=self.person_detailed)
        # another_imformation = Selector(response=response).xpath('//ul[@class="tinyTab datas_tabs"]/li')
        # for a in another_imformation:
        #     a_url = a.xpath('./a/@data-url').extract_first()
        #     span_person = a.xpath('./a/span/text()').extract_first()
        #     span_person = span_person.split(' ')[0]
        #     # print(span_person)
        #     if not a_url == None:
        #         if span_person == '个人工程业绩':
        #             a_url = self.big_url + a_url
        #             yield Request(url=a_url, callback=self.personal_merit)
        #
        #         elif span_person == '不良行为':
        #             a_url = self.big_url  + a_url
        #             yield Request(url=a_url, callback=self.personal_merit)
        #
        #         elif span_person == '良好行为':
        #             a_url = self.big_url + a_url
        #             yield Request(url=a_url, callback=self.personal_merit)
        #
        #         elif span_person =='黑名单记录':
        #             a_url = self.big_url + a_url
        #             yield Request(url=a_url, callback=self.personal_merit)
        #
        #         elif span_person == '变更记录':
        #             a_url = self.big_url + a_url
        #             yield Request(url=a_url, callback=self.change_person_data)

