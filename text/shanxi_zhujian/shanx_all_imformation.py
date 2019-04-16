import urllib.request
import urllib.parse
import json
import datetime
import redis
from . import setting

ALL_HEADER = setting.MY_USER_AGENT
import random
class shanxi_imformation(object):
    company_name = None
    tongna_api = None
    def random_header(self):
        header = random.choice(ALL_HEADER)
        return header
    # 查询公司
    def publicity_system(self, company_name):
        # company_name = '浙江大成工程项目管理有限公司'
        header = self.random_header()
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'User-Agent': header
        }
        data = {"searchword": company_name,
                "sourceType": "I"}
        zz = urllib.parse.urlencode(data).encode(encoding='UTF8')
        url = 'http://jzscyth.shaanxi.gov.cn:7001/PDR/network/informationSearch/informationSearchList?libraryName=enterpriseLibrary&pid1=610000'
        request = urllib.request.Request(url, headers=self.headers, data=zz)
        response = urllib.request.urlopen(request)
        json_data = response.read().decode('utf-8')
        self.now_company(json.loads(json_data))
        # print(json.loads(json_data))

    # 拿到查询到的公司
    def now_company(self, data):
        first_company = data['data']['result']['data'][0]
        one_nodenum = first_company['nodeNum']
        one_enttype = first_company['entType']
        one_pripid = first_company['pripid']
        url = 'http://app.gsxt.gov.cn/gsxt/corp-query-entprise-info-primaryinfoapp-entbaseInfo-' \
               + one_pripid + '.html?nodeNum=' + str(one_nodenum) + '&entType=' + str(one_enttype)
        all_company = urllib.request.Request(url, headers=self.headers)
        response = urllib.request.urlopen(all_company)
        html_data = response.read().decode('utf-8')
        zz = json.loads(html_data)
        self.send_data(zz)

    # 发送信息
    def send_data(self, data):
        company_dict = {}
        # 公司名称
        print(data)
        zz = data['result']
        company_dict['companyName'] = zz['entName']
        # 状态
        company_dict['regState_CN'] = zz['regState_CN']
        # 统一社会信用代码
        company_dict['uniscId'] = zz['uniscId']
        # 成立日期
        company_dict['estDate'] = zz['estDate']
        # 住所
        company_dict['dom'] = zz['dom']
        # 类型
        company_dict['entType_CN'] = zz['entType_CN']
        # 开始日期
        company_dict['opFrom'] = zz['opFrom']
        # 结束日期
        company_dict['opTo'] = zz['opTo']
        # 核准日期
        company_dict['apprDate'] = zz['apprDate']
        # 登记机关
        company_dict['regOrg_CN'] = zz['regOrg_CN']
        # 注册资本
        company_dict['entType_CN'] = zz['regCap']
        # 经营范围
        company_dict['opScope'] = zz['opScope']
        data_api = json.dumps(company_dict)
        print(data_api)
        # all_company = urllib.request.Request(self.tongna_api, headers=self.headers, data=data_api)
        # response = urllib.request.urlopen(all_company)
        # self.call_back(response)

    # 确认收到信息
    def call_back(self, call_data):
        print(call_data.read().decode('utf-8'))

    # 运行
    @classmethod
    def run_spider(self):
        new_time_error = datetime.datetime.now()
        new_zz = str(new_time_error)
        zz = new_zz.split('.')[0]
        zz = zz.replace(' ', '')
        zz = zz.replace('-', '')
        zz = zz.replace(':', '')
        zz = zz + '.txt'
        z = open(zz, 'a+', encoding="utf-8")
        for index, value in enumerate(self.company_name):
            index = str(index)
            try:
                yield self.publicity_system(value)
                content = value + '----添加成功' + index + '\n'
                z.write(content)
            except EOFError as e:
                content = value + e + '----失败' + index + '\n'
                z.write(content)
        z.close()
def run_spider():
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    company_list = []
    redis_len = r.scard('company_name')
    while redis_len != 0:
        for index in range(redis_len):
            if not index == 1000:
                name = r.spop("company_name")
                company_list.append(name)
            break
        tongna.company_name = company_list
        tongna_api = ''
        tongna.tongna_api = tongna_api
        tongna.run_spider()
        company_list = []

if __name__ == '__main__':
    run_spider()
    # zz = tongna()