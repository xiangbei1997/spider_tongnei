

class tongna(object):
    company_name = None
    tongna_api = None
    def run_spider(self):
        print(self.company_name, 'AAAA')
        print(self.tongna_api, 'BBBB')

my_list = []

for i in range(10):
    my_list.append(i)



tongna.company_name = my_list
# tongna.tongna_api = tongna_api
tongna.run_spider()