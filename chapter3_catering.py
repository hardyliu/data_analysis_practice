# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 14:43:13 2019

@author: hardyliu
"""

import pandas as pd

catering_sale = './chapter3/demo/data/catering_sale.xls'

data = pd.read_excel(catering_sale,index_col=u'日期')
print(data.describe())

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']

plt.rcParams['axes.unicode_minus']=False
plt.figure()
p = data.boxplot(return_type='dict') #画箱线图，直接使用DataFrame的方法

x = p['fliers'][0].get_xdata()
y = p['fliers'][0].get_ydata()

y.sort()#从小到大排序，该方法直接改变原对象

#用annotate添加注释
for i in range(len(x)): 
  if i>0:
    plt.annotate(y[i], xy = (x[i],y[i]), xytext=(x[i]+0.05 -0.8/(y[i]-y[i-1]),y[i]))
  else:
    plt.annotate(y[i], xy = (x[i],y[i]), xytext=(x[i]+0.08,y[i]))

plt.show()  


data = data[(data[u'销量']>400)&(data[u'销量']<5000)]#过滤异常数据
statistics = data.describe()

statistics.loc['range'] = statistics.loc['max']-statistics.loc['min'] #极差
statistics.loc['var'] = statistics.loc['std']/statistics.loc['mean'] #变异系数
statistics.loc['dis'] = statistics.loc['75%']-statistics.loc['25%'] #四分位数间距
print(statistics)      