# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 12:38:42 2019

@author: claireliu
"""

#模型构建

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans

inputfile = './tmp/zscoredata.xls'

data = pd.read_excel(inputfile)

k = 5

kmodel = KMeans(n_clusters = k,n_jobs=4)

kmodel.fit(data)

print("cluster center:",kmodel.cluster_centers_)

print("labels:",kmodel.labels_)

import numpy as np

plot_data = kmodel.cluster_centers_
#指定颜色
color = ['b', 'g', 'r', 'c', 'y'] 

angles = np.linspace(0, 2*np.pi, k, endpoint=False)
labels = data.columns 
# 闭合
plot_data = np.concatenate((plot_data, plot_data[:,[0]]), axis=1) 
# 闭合
angles = np.concatenate((angles, [angles[0]])) 

fig = plt.figure(figsize=(16,8))
#polar参数
ax = fig.add_subplot(111, polar=True) 

for i in range(len(plot_data)):
    linestyle = '.-' if i%2==0 else '--'#设置线条格式
    ax.plot(angles, plot_data[i], linestyle, color = color[i], label = 'client'+str(i), linewidth=2)

ax.spines['polar'].set_visible(False) # 将轴隐藏
ax.set_rgrids(np.arange(-1,2.5,0.5))
ax.set_thetagrids(angles * 180/np.pi, labels, fontproperties="SimHei")
plt.legend()
plt.show()

