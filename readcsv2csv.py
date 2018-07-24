# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 22:50:27 2018

@author: Administrator
"""

import pandas as pd

##整体思路(1)删除没用的数据或者是暂时停用这些数据
##（2）对这些数据进行整合处理

import os

dirpath = u"D:\\学习资料\\kesai\\天泽信息-人工智能大赛测试数据 7_2\\天泽信息-人工智能大赛测试数据 7_2\\testing_set_for_users.csv"

df_testdata = pd.read_csv(dirpath)
df_keyPoint = pd.read_csv(u"D:\\学习资料\\kesai\\天泽信息-人工智能大赛训练数据 7_2\\天泽信息-人工智能大赛训练数据 7_2\\dbd_faultcode.csv")

print df_keyPoint
#print df