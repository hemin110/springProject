# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

df_train = pd.read_csv('./train/dataset.csv',chunksize = 200000)
i=0
for chunk in df_train:
    i=i+1
    chunk.to_csv('./split2/'+str(i)+'_train.csv')
