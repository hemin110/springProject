# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 08:24:17 2018

@author: hemin
"""

import pandas as pd


for i in range(1,1):#11
    simpleData = pd.read_csv('./split2'+str(i)+'_train.csv')
    print (simpleData.head())

#simpleData = pd.read_csv('./split2/10_train.csv')
#
#tempDf = simpleData.dropna(axis = 1 , how = 'all')
#
#print (tempDf)
