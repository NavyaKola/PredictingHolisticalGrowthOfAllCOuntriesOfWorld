# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 03:02:55 2018

@author: navya
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def read_data(path):
    df=pd.read_csv(path)
    return df
df=read_data("C:\MS\DataIncubator\TS.csv")
required_df=read_data("C:\MS\DataIncubator\SR.csv")
required_ids=required_df['id']
df_required=df[df['id'].isin(required_ids)]
df_required.set_index('id',inplace=True)
df_required=df_required.transpose()
df_required=df_required.fillna(method='bfill')
#print(df_required.head())
#df_required.to_csv("required1.csv")
series = df_required[9918].head(36)
series=pd.to_numeric(series, downcast='float')
plot1=series.plot()
#print(df_required.iloc[38][1896])
plt.xlabel('Year', fontsize=14, color='Black')
plt.ylabel(df_required.iloc[38][9918], fontsize=9,color='Black')

plt.show()
