import pandas as pd  #数据框操作
import numpy as np
import matplotlib.pyplot as plt #绘图
import matplotlib as mpl #配置字体
from pyecharts import Geo  #地理图
import xlrd
import re




mpl.rcParams['font.sans-serif'] = ['SimHei'] #这个是绘图格式，不写这个的话横坐标无法变成我们要的内容
#配置绘图风格
plt.rcParams['axes.labelsize'] = 8.
plt.rcParams['xtick.labelsize'] = 12.
plt.rcParams['ytick.labelsize'] = 12.
plt.rcParams['legend.fontsize'] =10.
plt.rcParams['figure.figsize'] = [8.,8.]


data = pd.read_excel(r'E:\\scrapyanne\\lagou2\\lagou2\\spiders\\lagou2.xlsx',encoding='gbk') #出现错误的话试试utf8，路径不能出现中文，会出现错误


data['经验要求'].value_counts().plot(kind='barh')  #绘制条形图
plt.show   #显示图片

data['工作地点'].value_counts().plot(kind='pie',autopct='%1.2f%%',explode=np.linspace(0,1.5,32))
plt.show   #显示图片

#从lambda一直到*1000，是一个匿名函数，*1000的原因是这里显示的是几K几K的，我们把K切割掉，只要数字，就*1000了
data2 = list(map(lambda x:(data['工作地点'][x],eval(re.split('k|K',data['薪资待遇'][x])[0])*1000),range(len(data))))


#再把data2框架起来
data3 = pd.DataFrame(data2)
data3


#转化成geo所需要的故事，也是用匿名函数，在data3中，按照地区分组，然后根据地区来计算工资的平均值，将其变成序列后再分组
data4 = list(map(lambda x:(data3.groupby(0).mean()[1].index[x],data3.groupby(0).mean()[1].values[x]),range(len(data3.groupby(0)))))


#geo = Geo('主标题','副标题',字体颜色='白色',字体位置='中间'，宽度=1200,高度=600,背景颜色=‘#404a59')
geo = Geo("全国数据分析工资分布", "制作:风吹白杨的安妮", title_color="#fff", title_pos="center",width=1200, height=600, background_color='#404a59')

#属性、数值对应的映射关系,attr是属性,value是该属性对应的数值，比如说北京对应15000，杭州对应10000
attr, value =geo.cast(data4)

#这个是对地图进行设置，第一个参数设置为空值，我看别人这么设置我也这么设置了，下次查查为什么，第二个参数是属性，第三个为对应数值，
#第四个参数是可视范围,把工资区间换算成了0到300. 第五个很容易出错，我之前安装完地图还是出错的原因就是没加上maptype=''china',一定要加上，第六个图例类型写上热力图，
#第七个参数是地图文本字体颜色为白色，第八个是标识大小，第九个是否进行可视化=True.
geo.add("", attr, value, visual_range=[0, 300],maptype='china',type='heatmap' ,visual_text_color="#fff", symbol_size=15, is_visualmap=True)

geo