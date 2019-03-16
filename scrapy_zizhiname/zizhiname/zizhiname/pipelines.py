# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ZizhinamePipeline(object):
    def __init__(self,*args,**kwargs):
            self.f = open('xinliang.txt', 'a',encoding='UTF-8')
            self.name = set()
    def process_item(self, item, spider):
        # print(item['name'], '此公司已经添加到了')
        if not item['name'] in self.name:
            self.name.add(item['name'])
            self.f.write(item['name']+'\n')
        return item

    # def open_spider(self, spider):
    def spider_closed(self, spider):
        self.f.close()

