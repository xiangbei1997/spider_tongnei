# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MytuneiPipeline(object):
    def process_item(self, item, spider):
        return item


import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline


class PicsDownloadPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['myimg']:
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        # 将下载的图片路径（传入到results中）存储到 image_paths 项目组中，如果其中没有图片，我们将丢弃项目:
        image_path = [x['path'] for ok, x in results if ok]
        if not image_path:
            raise DropItem("Item contains no images")
        item['image_path'] = image_path
        return item


# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from twisted.enterprise import adbapi
# import MySQLdb
# import MySQLdb.cursors
from scrapy.crawler import Settings as settings
class xiaohuaPipeline(object):
    def __init__(self,*args,**kwargs):
            self.f = open('xiaohua.json', 'a')
    def __init__(self,bd):
        self.bd = bd
    @classmethod
    def from_spider(cls,crawler):
       open_bd = crawler.setting.get('DB')
       return cls(open_bd)
    def open_spider(self,spider):
        dbargs = dict(
                host = 'your host',
                db = 'crawed',
                user = 'user_name',  # replace with you user name
                passwd = 'user_password',  # replace with you password
                charset = 'utf8',
                cursorclass = MySQLdb.cursors.DictCursor,
                use_unicode = True,
                 )
        self.dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)
        res = self.dbpool.runInteraction(self.insert_into_table)
    def close_spider(self,spider):
        pass
    def process_item(self, item, spider):
       f = open('xiaohua.json','a')
       tp1 = "%s\t%s\n%\n\n\n" % (item['uname'], item['school'], item['img_url'])
       f.write(tp1)
       f.close()

class seexiaohuaPipeline(object):
    def process_item(self, item, spider):
        print(spider)
        print(item['uname'], item['school'], item['img_url'])



import pymysql

def dbHandle():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        passwd='root',
        charset='utf8',
        use_unicode=False
    )
    return conn

class HelloPipeline(object):
    def process_item(self, item, spider):
        dbObject = dbHandle()
        cursor = dbObject.cursor()
        sql = 'insert into joke.t_baike(userIcon,userName,content,likes,comment) values (%s,%s,%s,%s,%s)'

        try:
            cursor.execute(sql,(item['userIcon'],item['userName'],item['content'],item['like'],item['comment']))
            dbObject.commit()
        except Exception as e:
            print(e)
            dbObject.rollback()
#
#         return item


from scrapy import signals
import json
import codecs
from openpyxl import Workbook
class LagouPipeline(object):
    def __init__(self):
        self.workbook = Workbook()
        self.ws = self.workbook.active
        self.ws.append(['公司名称', '工作地点', '职位名称', '经验要求', '薪资待遇'])  # 设置表头
        self.file = codecs.open('lagou2.json', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        line = [item['name'], item['location'], item['position'], item['exprience'], item['money']]  # 把数据中每一项整理出来
        self.ws.append(line)
        self.workbook.save('lagou2.xlsx')  # 保存xlsx文件
        #line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        #self.file.write(line)
        return item
    def spider_closed(self, spider):
        self.file.close()


    

