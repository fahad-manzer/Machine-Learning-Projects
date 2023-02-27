# -*- coding: utf-8 -*-
"""Stocks Price Analysis GOOG-VIX.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kgaAw7DmaaBN-8iFor-Pg6lWD8_LbOJB
"""

!pip install yfinance

import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns

df=yf.download(['GOOG','^VIX'],
               start='2000-01-01',
               end='2023-02-24',
               progress=False)

df

df=df[['Adj Close']]
df

df.columns=df.columns.droplevel(0)
df.columns

df=df.rename(columns={'GOOG':'goog','^VIX':'VIX'})

df

df.head()

df.tail()

df['log_rtn']=np.log(df.goog/df.goog.shift(1))
df['log_rtn']

df['VIXlog_rtn']=np.log(df.VIX/df.VIX.shift(1))
df['VIXlog_rtn']

df['log_rtn'],df['VIXlog_rtn']

df.dropna(how='any',axis=0,inplace=True)

df.dropna()

corr_coeff=df.log_rtn.corr(df.VIXlog_rtn)

corr_coeff

ax=sns.regplot(x='log_rtn',color='red',y='VIXlog_rtn',data=df,line_kws={'color':'green'})
ax.set(title=f'GOOG VS VIX ($\\rho$={corr_coeff:.2f})')