# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 11:11:27 2019

@author: claireliu
"""

import pandas as pd
import numpy as np

cleanedfile = './tmp/data_cleaned.csv'
score_data_file = './tmp/score_data.csv'

data_ori = pd.read_csv(cleanedfile,encoding='utf-8')

print(data_ori.describe().T)

#属性选择
feaures_slect = ['LOAD_TIME','FFP_DATE','FLIGHT_COUNT','avg_discount','SEG_KM_SUM','LAST_TO_END']


data =data_ori[feaures_slect]

data['LOAD_TIME'] = pd.to_datetime(data['LOAD_TIME'])
data['FFP_DATE'] = pd.to_datetime(data['FFP_DATE'])
data['L']=(data['LOAD_TIME']-data['FFP_DATE'])
data.L=data.L.map(lambda x: x/np.timedelta64(1*60*60*24*30, 's'))

data.rename(columns={'LAST_TO_END':'R','FLIGHT_COUNT':'F','SEG_KM_SUM':'M','avg_discount':'C'},inplace=True)

columns = data.columns.tolist()
for x in ['LOAD_TIME','FFP_DATE']:
    columns.remove(x)


data = data[columns]

data.to_csv(score_data_file,index=False,encoding='utf-8')


z_score_file = './tmp/zscoredata.xls'

data_score = (data-data.mean(axis=0))/(data.std(axis=0))

data_score.columns=['Z'+i for i in data.columns]#重新命名列
data_score.to_excel(z_score_file,index=False)



