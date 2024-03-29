# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Problem Set 1 - Kyle Bailey, Danielle Bauer

# Import packages
import numpy as np
import pandas as pd
import os
from statsmodels.formula.api import ols
from scipy.stats import pearsonr
 
os.chdir('/Users/Kyle/Desktop/Python/Data')

# Question 1

# Read BWGHT data
df1 = pd.read_csv('/Users/Kyle/Desktop/Python/Data/BWGHT.csv')
df1.head()

# (ii)
pearsonr(df1['cigs'],df1['faminc']) 

# (iii)
m1_1 = ols('bwght ~ cigs + faminc', data=df1).fit() 
m1_1.summary()
# Regression without family income
m1_2 = ols('bwght ~ cigs', data=df1).fit() 
m1_2.summary()

# Question 3

# Read CEOSAL2 data
df3 = pd.read_csv('/Users/Kyle/Desktop/Python/Data/CEOSAL2.csv')
df3.head()

# (i)
log_sales = np.log(df3['sales'])
log_mktval = np.log(df3['mktval'])
m3_1 = ols('salary ~ log_sales + log_mktval', data=df3).fit()
m3_1.summary()

# (ii)
m3_2 = ols('salary ~ log_sales + log_mktval + profits', data=df3).fit()
m3_2.summary()

# (iii)
m3_3 = ols('salary ~ log_sales + log_mktval + profits + ceoten', data=df3).fit()
m3_3.summary()

# (iv)
pearsonr(df3['log_mktval'],df3['profits']) 

# Question 4

# Read ATTEND data
df4 = pd.read_csv('/Users/Kyle/Desktop/Python/Data/ATTEND.csv')
df4.head()

# (i)
df4['atndrte'].min()
df4['atndrte'].max()
df4['atndrte'].mean()

df4['priGPA'].min()
df4['priGPA'].max()
df4['priGPA'].mean()

df4['ACT'].min()
df4['ACT'].max()
df4['ACT'].mean()

# (ii)
m4_1 = ols('atndrte ~ priGPA + ACT', data = df4).fit()
m4_1.summary()

# (iv)
p1 = pd.DataFrame({'priGPA': [3.65], 'ACT': [20]})
p1
m4_1.predict(p1)

# (v)
p2 = pd.DataFrame({'priGPA': [3.1, 2.1], 'ACT': [21, 26]})
p2
m4_1.predict(p2)

# Question 7

# Read MEAP93 data
df7 = pd.read_csv('/Users/Kyle/Desktop/Python/Data/MEAP93.csv')
df7.head()

# (i)
log_expend = np.log(df7['expend'])
m7_1 = ols('math10 ~ log_expend + lnchprg')
m7_1.summary()