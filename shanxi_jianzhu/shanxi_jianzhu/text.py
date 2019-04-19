import redis
import json
pool = redis.ConnectionPool(host='106.12.112.205', password='tongna888')
r = redis.Redis(connection_pool=pool)
len_company = r.scard('all_company_name')
# zz = r.scard('keep_on_record_person')
print(len_company)
# person = r.scard('title_renyuan')
# print(len_company)
# print(person)
# zz = r.spop('title_102')
# print(zz)
# data = json.loads(zz)
# print(data)
# print(len_company)
# zz = r.sadd('hebei', 'ZZZZZZZZZZZZZZZ')
# print(zz)
# print(len_company)
# for i in range(140):
#     mylen = r.spop('another_province_into_see')
# len_company = r.scard('another_province_into_see')
# print(len_company)
# len_company = r.spop('another_into_hebei')
# print(len_company)
import random
# import re
# zz = {}
# zz['i'] = re.escape('2')
# zz['c'] = re.escape('76')
# zz['p'] = re.escape('15')
# zz['s'] = re.escape(' and  t1.FId=t3.FBaseInfoId and t1.FIsDeleted=0  and t3.FIsDeleted=0 and t1.FState=2 ')
# no_zz = random.random()
# no_zz = str(no_zz)
# zz['e'] = re.escape(no_zz)
# print(zz)

# for i in range(2,77):
#     print(i)

#
# import os
#
# from apscheduler.schedulers.blocking import BlockingScheduler
# sched = BlockingScheduler()
# def fun_min():
#     os.system('scrapy crawl person_ok')
#
# fun_min()
# sched.add_job(fun_min, 'interval', hours=24)
# sched.start()


# for i in range(1, 29):
#     print(i)

# import time
#
# # print(time.time())
# zzz = time.time() * 1000
# zzz = int(zzz)
# print(zzz)
# # 1554342639259
# # 1554342637436
# # 1554341673092
#
# G = 1554342637436 - 1554341673092
# print(G)
# 964344
# 1000000


# # print(zzz)
#
# for i in range(2, 127):
# #     print(i)
# import random
# zz = random.randint(1,5)
# print(zz)
# a = [1,4,7,9]
# del a[0]
# print(a)


# sd = '4208811000917'
# print(len(sd))



# import re
# zz = 'ShowWin\(\'(.*)\',\'(.*)\',\'v\'\);return false;'
# a = 'ShowWin(\'0135EA69-F621-4F20-A578-A409D619509D\',\'913408811539111982\',\'v\');return false;'
# "background-image: url\(\"(.*)\"\); background-position: (.*)px (.*)px;"
# m = re.findall(zz, a)
# print(m[0][0])

# zz = '1251000045072011X8'
# print(len(zz))
#
# import re
#
# zz = 'OpenCorpDetail(\'9121030068661847X7\',\'9121030068661847X7\',\'鞍钢贝克吉利尼水处理有限公司\')'
# s = 'OpenCorpDetail\(\'(.*)\',\'(.*)\',\'(.*)\'\)'
# data = re.findall(s, zz)
# print(data)


# http://115.29.2.37:8080/enterprise_detail.php?CORPCODE=MA2CPRDE-9
# http://115.29.2.37:8080/enterprise_detail.php?CORPCODE=MA2AQFTL-9
# http://115.29.2.37:8080/enterprise_detail.php?CORPCODE=58652498-6

# heands = {
# 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
# 'Accept-Encoding': 'gzip, deflate',
# 'Accept-Language': 'zh-CN,zh;q=0.9',
# 'Connection': 'keep-alive',
# 'Cookie': 'PHPSESSID=ocb0db6p0118st4ptqbqhasd30',
# 'Host': '115.29.2.37:8080',
# 'Referer': 'http://115.29.2.37:8080/enterprise.php',
# 'Upgrade-Insecure-Requests': '1',
# 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
# }
#
# print(len('91361000589220101B'))
# import re
# # zz = 'ShowWin(&#39;DAF87B17-51A6-42A4-AD21-0F785204F278&#39;,&#39;91350100777536998F&#39;,&#39;v&#39;)'
# # ww = 'ShowWin\(&#39;(.*)&#39;,&#39;(.*)&#39;,&#39;v&#39;\)'
# zz = 'ShowWin(\'7D0896AA-62A2-4BC9-AC9E-5DBBFDC21CFD\',\'91320508768275933R\',\'v\');return false;'
# ww = 'ShowWin\(\'(.*)\',\'(.*)\',\'v\'\);return false;'
#
#
#
# # ww = 'ShowWin\(&#39;(.*);,&#39;(.*);,&#39;v&#39;\)'
#
#
# a = re.findall(ww, zz)
# print(a)
# # http://221.214.94.41:81/InformationReleasing/Ashx/InformationReleasing.ashx?callback=jQuery17105832114001259432_1555134365895&methodname=getoutprovincecorpinfo&CorpName=&CorpCode=&DanWeiType=&CurrPageIndex=3&PageSize=12&_=1555135075508
# http://221.214.94.41:81/InformationReleasing/Ashx/InformationReleasing.ashx?callback=jQuery171016828268477252095_%s&methodname=GetCorpInfo&CorpName=&CorpCode=&CertType=&LegalMan=&CurrPageIndex=%s&PageSize=%s


# /

# import re
# zz = '【共4283条数据 第1/429页】  '
# re_pagenumber = '【共\d+条数据 第1/(.*)页】  '
# AAA = re.findall(re_pagenumber, zz)[0]
# print(AAA)
# print(len(zz))

# 230000

# zz = ' '
# print(zz,'AAAAAAAA')
#
# if self.flag:
#     for i in range(1, 279):
#         if i == 278:
#             self.flag = False
#         yield scrapy.Request(url=self.url + '?p=%s' % i, callback=self.parse)
# mylist = ['http://59.175.169.110/web/QyManage/QyList.aspx?qylx=1',
#   'http://59.175.169.110/web/QyManage/QyList.aspx?qylx=2',
#   'http://59.175.169.110/web/QyManage/QyList.aspx?qylx=3',
#   'http://59.175.169.110/web/QyManage/QyList.aspx?qylx=4',
#   'http://59.175.169.110/web/QyManage/QyList.aspx?qylx=5',
#   'http://59.175.169.110/web/QyManage/QyList.aspx?qylx=6',
#   'http://59.175.169.110/web/QyManage/QyList.aspx?qylx=7']


# mylis = [{'http://59.175.169.110/web/QyManage/QyList.aspx?qylx=8': 1},
#           {'http://59.175.169.110/web/QyManage/QyList.aspx?qylx=9': 1},
#           {'http://59.175.169.110/web/QyManage/QyList.aspx?qylx=10': 1},
#           {'http://59.175.169.110/web/QyManage/QyList.aspx?qylx=11': 1},
#           {'http://59.175.169.110/web/QyManage/QyList.aspx?qylx=12': 1},
#           {'http://59.175.169.110/web/QyManage/QyList.aspx?qylx=13': 1},
#            {'http://59.175.169.110/web/QyManage/QyList.aspx?qylx=14]': 1}
#           ]
#
#
# import re
#
# gg = 'http://59.175.169.110/web/QyManage/QyList.aspx?qylx=4'
# now_number = 'http://59.175.169.110/web/QyManage/QyList.aspx\?qylx=(\d)'
# zz = re.findall(now_number, gg)[0]
# print(zz)
# print(type(zz))


# aa = [1,4,2,6,7,9,0,3,2,5]
#
# for i in range(len(aa)):
#     print(i)
# print(len(aa))
# import  re
# zz = 'winopen(\'enterpriseInfoViewActionOut\?enterpriseInfo\.id=24\&enQualificationType=DIC0002001&institution\.id=2141\&userId=2523181\&outQueryFlag=\',1100,600,\'详情\');'
# # zz = 'winopen\(\'enterpriseInfoViewActionOut?enterpriseInfo\.id=21&enQualificationType=DIC0002001&institution.id=21&userId=2392092&outQueryFlag=\',1100,600,\'详情\'\);'
# qq = 'winopen\(\'(.*)\',1100,600,\'详情\'\);'
# mytest = re.findall(qq, zz)
# print(mytest)

# zz = None
# print(len(zz))
import requests
import json

# data = {'companyName': '湖南楚瑞工程咨询有限公司', 'licenseNum': '91430111572226566N', 'area': '湖北省', 'major': '', 'regNum': '', 'validTime': '',
#         'tokenKey': 'LnHRF8R1jmqOLFnnK048DcokeilQRDS2', 'name': '刘敏', 'sex': '男',
#         'idCard': '430304**********57', 'grade': '造价工程师', 'num': '建[造]09430004686'}
#
# zz = requests.post(url='http://192.168.199.188:8080/web/rest/companyInfo/addCompanyRecordEngineer.htm',
#               data=data
#               )
# print(zz)
import time
c = time.localtime(1483545600)
# #
now_c = time.strftime("%Y-%m-%d", c)
print(now_c)
# print(len('120225198609263188'))