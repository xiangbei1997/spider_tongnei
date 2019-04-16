# # /home/www/spider_rizhi
#
#
# f = open('/home/www/spider_rizhi/20190330143446.log', 'r', encoding='utf-8')
# # while True:
# # INFO: 对不起，未查询到此公司的信息
# # ERROR: {"msg":"成功","code":0}
# ok_data = []
# error_data = []
# one_line = f.readline()
# # 2019-03-30 14:42:00 [root] ERROR: {"msg":"成功","code":0}
# # 2019-03-30 14:59:54 [root] ERROR: 对不起，未查询到此公司的信息
# ok_data_re =re.compile( r'\d+-\d+-\d+ \d+:\d+:\d+ [root] ERROR: {"msg":"成功","code":0}')
# fail_data_re = r'\d+-\d+-\d+ \d+:\d+:\d+ [root] ERROR: 对不起，未查询到此公司的信息'
# import re
# while one_line:
#    if re.search(ok_data_re):
#        error_data.append(one_line)
#        print(one_line)
#    elif re.search(fail_data_re):
#        ok_data.append(one_line)
#        print(one_line)
# print(ok_data)
# print(error_data)
#
#
# # ['_DEFAULT_ENCODING', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__'
# # , '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '
# # __setattr__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', '__weakref__', '_auto_detect_fun', '_body', '_body_declared_encoding', '_b
# # ody_inferred_encoding', '_cached_benc', '_cached_selector', '_cached_ubody', '_declared_encoding', '_encoding', '_get_body', '_get_url', '_headers
# # _encoding', '_set_body', '_set_url', '_url', ]
#
#
# text = 'javascript:location.href=\'/dataservice/query/comp/compDetail/170527180413881327\''
#
# re_a = 'javascript:location.href=\'(.*)\''

zz = '915101000500952718'
print(len(zz))