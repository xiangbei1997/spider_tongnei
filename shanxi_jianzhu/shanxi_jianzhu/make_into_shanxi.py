import os



def fun_min():
    os.system('scrapy crawl another_province_into_zhejiang.py')
fun_min()
# sched.add_job(fun_min, 'interval', hours=24)
# sched.start()