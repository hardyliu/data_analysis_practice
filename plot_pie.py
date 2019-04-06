# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 16:54:24 2019

@author: hardyliu
"""
import matplotlib.pyplot as plt


labels = 'Frogs','Hogs','Dogs','Logs'

sizes = [15,30,45,10]

colors = ['yellowgreen','gold','lightskyblue','lightcoral']

explode = (0,0.1,0,0)#突出显示Hogs

plt.pie(sizes,explode=explode,colors=colors,labels=labels,shadow=True,autopct='%1.1f%%',
        startangle=180)

plt.axis('equal')
plt.show()