#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 09:31:23 2019

@author: Tamara Williams
"""

import pandas as pd
import time
import os

dt = time.strftime('%Y-%m-%d', time.localtime())



datapath = '~/Disney_Tweets/data/tmp/'
outpath = '~/Disney_Tweets/data/daily/'
daily = pd.DataFrame([])

directory = os.fsencode(datapath)

for file in os.listdir(directory):
     filename = os.fsdecode(file)
     print(filename)
     if filename.endswith(".csv"): 
         tmp = pd.read_csv(datapath + filename)
         print(tmp)
         daily = daily.append(tmp,ignore_index=True)
         continue
     else:
         continue
         
tmp2 = daily.drop_duplicates(subset=None, inplace=False)
      

filename = outpath+'clean'+dt+'.csv'
tmp2.to_csv(filename, sep=',', date_format = 'string', index = False, encoding = 'utf-8')
