# -*- coding: utf-8 -*-
import scrapy
from scrapy import  Selector
from scrapy.http import Request,Response
class AllXinliangSpider(scrapy.Spider):
    # 执行名称
    name = 'concise'
    def start_requests(self):
        # 起始url
        self.big_url = 'http://jzsc.mohurd.gov.cn'
        # form表单url
        self.url = 'http://jzsc.mohurd.gov.cn/dataservice/query/comp/list'
        # 提交form数据
        self.corporate_name = '汶上县建筑设计院有限公司'
        # 访问并携带参数
        return [scrapy.FormRequest(self.url,
                                   formdata={'qy_name': self.corporate_name},
                                   callback=self.parse)]
    def parse(self, response):
        # 进入当前公司
        corporate_url = Selector(response=response).xpath('//td[@class="text-left primary"]/a/@href').extract_first()
        url = self.big_url + corporate_url
        return Request(url=url,callback=self.detailed_information)


    def detailed_information(self, response):
        from ..items import  ZizhinameItem
        # 创建存储所有数据的字典
        self.company_dir = {}
        # 获取当前公司名称
        self.company_information = Selector(response=response).xpath('//div[@class="user_info spmtop"]/b/text()').extract_first()
        # 根据公司名称创建所有数据
        self.company_dir[self.company_information] = {}
        # 获取公司基本信息
        table_information = Selector(response=response).xpath('//table[@class="pro_table_box datas_table"]/tbody/tr')
        for t in table_information:
            # 公司key
            table_hand = t.xpath('./td/@data-header').extract_first()
            # 去除空格
            if not table_hand == None:
                table_hand = table_hand.split()[0]
            # print(type(table_hand))
            # 公司value
            table_body = t.xpath('./td/text()').extract_first()
            # 去除空格
            if not table_body == None:
                table_body = table_body.split()[0]
            # 添加进字典
            self.company_dir[self.company_information][table_hand] = table_body
        #     获取全部js请求的li
        enterprise_url = Selector(response=response).xpath('//ul[@class="tinyTab datas_tabs"]/li')
        for e in enterprise_url:
            # 拿到需要请求的地址来进行操作
            url = self.big_url + e.xpath('./a/@data-url').extract_first()
            # 拿到所属名称
            self.span = e.xpath('./a/span/text()').extract_first()
            # 去掉空格
            self.span = self.span.split()[0]
            # 创建可存放重复数据的列表
            self.company_dir[self.company_information][self.span] = []
            # 使用item传递数据
            name = ZizhinameItem(name=self.span)
            # 拿到数据相关信息进行操作用
            yield Request(url=url, callback=self.zz,meta={'item': name})
    def zz(self,response):
        # 获取当前全部TR -- 每一行的数据
        content = Selector(response=response).xpath("//tbody/tr")
        for c in content:
            # 每一行的数据
            all_td = c.xpath('./td')
            # 把没次获取的一行的数据保存成一行
            my_all = {}
            for a in all_td:
                # 每个Td的内容
                head = a.xpath('./@data-header').extract_first()
                # 如果是名字的话就获取a标签的内容
                if head == '姓名':
                    body = a.xpath('./a/text()').extract_first()
                # 如果是资质名称的话就获取去除\n\r\t
                elif head == '资质名称':
                    body = a.xpath('./text()').extract_first()
                    body = body.split()[0]
                # 出过以上两种特殊情况外，其他全部不变
                else:
                    body = a.xpath('./text()').extract_first()
                #  添加数据到一行数据里
                my_all[head] = body
            # 然后添加进大的字典里
            self.company_dir[self.company_information][response.meta['item']['name']].append(my_all)
        return self.text()



    def text(self):
        print(self.company_dir)

#         这是工程项目的请求
# url = 'http://jzsc.mohurd.gov.cn/dataservice/query/comp/compPerformanceListSys/001607220057227232'
# 这是项目详细的介绍地址
# project_make = 'http://jzsc.mohurd.gov.cn/dataservice/query/project/projectDetail/3708301603280101'