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
from statsmodels.stats.outliers_influence import variance_inflation_factor
 
os.chdir('/Users/Kyle/Desktop/Python/Data')

# Question 1

# Read BWGHT data
df1 = pd.read_csv('BWGHT.csv')
df1.head()
df1.isnull().sum()

# Question 1(i)
# The most likely sign for B2 is positive, if birth weights are correlated with better prenatal care, 
# then having higher family income allows access to these resources leading to higher birth weights in turn

# Question 1(ii)
# cigs and faminc are likely to be loosely negatively correlated. Higher family income allows better medical 
# care and education that bring awareness to the dangers of cigarette smoking. This is confirmed by a Pearson 
# correlation coefficient of -0.17.
pearsonr(df1['cigs'],df1['faminc']) 

# Question 1(iii)
m1_1 = ols('bwght ~ cigs + faminc', data=df1).fit() 
m1_1.summary()
# bwght = 116.9741 -0.4634cigs + 0.0928faminc, n = 1388, r2 = 0.03
# Regression without family income
m1_2 = ols('bwght ~ cigs', data=df1).fit() 
m1_2.summary()
# bwght = 119.7719 -0.5138cigs, n = 1388, r2 = 0.023
# The regression results are certainly different, although not to a very high degree. The coefficient
# on cigs only changes from -0.46 to -0.51 (a one oz increase in birth is associated with ~.5 less cigarettes per day)
# Additionally, the fit of the model decreased only by 0.01 but with an r2 of less than .1 the explanatory power
# of the models are quite weak

# Question 3

# Read CEOSAL2 data
df3 = pd.read_csv('CEOSAL2.csv')
df3.head()
df3.isnull().sum()

# Question 3(i)
m3_1 = ols('lsalary ~ lsales + lmktval', data=df3).fit()
m3_1.summary()
# lsalary = 4.6209 + 0.1621lsales + 0.1067lmktval

# Question 3(ii)
m3_2 = ols('lsalary ~ lsales + lmktval + profits', data=df3).fit()
m3_2.summary()
# We cannot include profits in this model as due to them being measured in millions, with the rest of the equation in log
# form, the coefficient is extrordinarily small and statistically insignificant as well. Additionally, several firms
# in the dataset had negative profits (losses) such that trying to calculate lsalary will lead to it being undefined
# Given the r2 is roughly 0.30, I would say that this model does not capture most of the variation in CEO salaries 
# as we can only explain 30% of salary variation, including more variables would help us more clearly see the effects.

# Question 3(iii)
m3_3 = ols('lsalary ~ lsales + lmktval + profits + ceoten', data=df3).fit()
m3_3.summary()
# Holding all other factors fixed, if CEO tenure increases by 1 year, lsalary will increase by 1.17% 
# Question 3(iv)
pearsonr(df3['lmktval'],df3['profits']) 
# The Pearson R coefficient between log(market value) and profits is 0.78, this implies strong correlation between
# the two variables and likely collinearity within the model. Higher profits are generally associated with higher
# market value so including both would be difficult to capture the individual effects without OLS estimators 
# being biased.

# Question 4

# Read ATTEND data
df4 = pd.read_csv('ATTEND.csv')
df4.head()
df4.isnull().sum()

# Question 4(i)
df4['atndrte'].min()
# 6.25
df4['atndrte'].max()
# 100.0
df4['atndrte'].mean()
# 81.71

df4['priGPA'].min()
#0.8570
df4['priGPA'].max()
# 3.9300
df4['priGPA'].mean()
# 2.5868

df4['ACT'].min()
# 13
df4['ACT'].max()
# 32
df4['ACT'].mean()
# 22.5103

# Question 4(ii)
m4_1 = ols('atndrte ~ priGPA + ACT', data = df4).fit()
m4_1.summary()
# atndrte = 75.7004 + 17.2606priGPA - 1.7166ACT
# The intercept states that a student with a 0.0 GPA the previous term and a 0 ACT score will attend, on average,
# around 75% of their classes. I don't believe that it is useful in this case as any students who have these characteristics
# will likely be removed from school in a practical setting.

# Question 4(iii)
# The coefficient on priGPA makes sense as a one unit increase in GPA (1.0/4.0 scale) is responsible for a 17% increases in attendance
# rate, all else held equal. Students who get higher grades are far more likely to go to class more consistently.
# The coefficient on ACT was suprising, however, as its sign was negative when I expected it to be positive. Additionally,
# the magnitude implied for a 1 unit increase in score (out of 36), attendance rate dropped 1.7%, all else held equal. 
# Students who perform higher on tests should generally be overall higher performing students.

# Question 4(iv)
p1 = pd.DataFrame({'priGPA': [3.65], 'ACT': [20]})
p1
m4_1.predict(p1)
# 104.37
# This result is not possible in the dataset given the maximum attendance rate is 100% (all 32 classes attended)
# Additionally, there are no students in the sample with those values of explanatory variables

# Question 4(v)
p2 = pd.DataFrame({'priGPA': [3.1, 2.1], 'ACT': [21, 26]})
p2
m4_1.predict(p2)
# Student A: 93.1606
# Student B: 67.3173
print(93.1606-67.3173)
# 25.8433
# Student A is predicted to attend ~25% more classes than Student B

# Question 7

# Read MEAP93 data
df7 = pd.read_csv('MEAP93.csv')
df7.head()
df7.isnull().sum()

# Question 7(i)
m7_1 = ols('math10 ~ lexpend + lnchprg', data = df7).fit()
m7_1.summary()
# math10 = -20.3607 + 6.2297lexpend - 0.3046lnchprg, n = 408, r2 = 0.180
# The sign on the lexpend I expected to be positive, as higher spending within a school per student
# will likely lead to higher math scores due to better quality teaching and materials.
# The sign on lnchprg I also expected to be negative, as students whose are on lunch programs are far more
# likely to be from lower income families in districts with much lower access to resources.

# Question 7(ii)
# It does not make sense to set the explanatory variable lexpend to 0. Setting it to 0
# would be equivilant to setting expend = 1, which implies that a school is only spending $1 per student
# when the minimum value for expendature per student is $3332 in the dataset.
# Setting lnchprg to 0 makes more sense as it could be a very high income school district where students do
# not need to be on a school lunch program.
df7['expend'].min()
# Having a negative intercept is not really indicitive of anything given the data, as it does not make sense
# to have -20% of students passing MEAP math if the explanatory variables are set to 0.

# Question 7(iii)
m7_2 = ols('math10 ~ lexpend', data = df7).fit()
m7_2.summary()
# math10 = -69.3411 + 11.1644lexpend
# The slope coefficient on lexpend has increased from 6.2297 to 11.1644, a 0.05% increase in MEAP math scores 
# per dollar spent on students

# Question 7(iv)
pearsonr(df7['math10'], df7['lexpend'])
# 0.1722
# Having math10 and lexpend being positively correlated makes sense to me given that access to better 
# resources will generally allow students to perform better.

# Question 7(v)
# Because the two variables are positively correlated, having solely lexpend in a regression will yield a 
# more pronounced spending effect because it is capturing the variation in both.

#Question 8
df8 = pd.read_csv('DISCRIM.csv')
df8.head()
df8.describe()

df8.isnull().sum()
df8 = df8.dropna(subset=['income', 'prpblck', 'psoda', 'prppov'])
df8.isnull().sum()

#Question 8(i)
print(np.mean(df8.prpblck))
#0.11495511886262233
print(np.mean(df8.income))
#46999.40399002494
print(np.std(df8.prpblck))
#0.18364563522127417
print(np.std(df8.income))
#13198.845626293141
#income is in dollars & prpblck is a percentage

#Question 8(ii)
m8_1 = ols('psoda ~ prpblck + income', data=df8).fit() 
m8_1.summary()
#psoda = 0.9563 + 0.1150*prpblck + 0.000001603*income
#R-Squared = 0.064
#Sample Size = 401
#Holding income constant, if prpblock increases by one percent,
#psoda increases by 0.1150
#Yes, an increase in soda price of $0.11 does seem significant 

#Question 8(iii)
m8_2 = ols('psoda ~ prpblck', data=df8).fit() 
m8_2.summary()
#The discrimination effect (0.0649) is smaller without income

#Question 8(iv)
m8_3 = ols('np.log(psoda) ~ prpblck + np.log(income)', data=df8).fit() 
m8_3.summary()
#log(psoda) = -0.7938 + 0.1216*prpblck + 0.0765*log(income)
#R-Squared = 0.068
#Sample Size = 401
#2.43%

#Question 8(v)
m8_4 = ols('np.log(psoda) ~ prpblck + np.log(income) + prppov', data=df8).fit() 
m8_4.summary()
#The coefficient for prpblck decreases to 0.0728

#Question 8(vi)
df8.income_log = np.log(df8.income)
pearsonr(df8.income_log,df8.prppov)
#Corr Coeff = -0.8402068944304426 w/ p-value = 4.2371233881359175e-108
#Yes, I assumed that proportion in poverty and income would be highly, 
#negatively correlated (the higher proportion in poverty, the lower the income)

#Question 8(vii) 

variables = m8_4.model.exog
vif = [variance_inflation_factor(variables, i) for i in range(variables.shape[1])]
vif 
#Not necessarily true, it depends on their VIF (they both have VIF < 10)

#Question 9
df9 = pd.read_csv('CHARITY.csv')
df9.head()
df9.describe()

df9.isnull().sum()

#Question 9(i)
m9_1 = ols('gift ~ mailsyear + giftlast + propresp', data=df9).fit() 
m9_1.summary()
#gift = -4.5515 + 2.1663*mailsyear + 0.0059*giftlast + 15.3586*propresp
#R-Squared = 0.083
#Sample Size = 4268

m9_2 = ols('gift ~ mailsyear', data=df9).fit() 
m9_2.summary()
#gift = 2.0141 + 2.6495*mailsyear
#R=Squared decreased to 0.014

#Question 9(ii)
#In the multiple regression, holding giftlast and propresp constant, if 
#mailsyear increases by one unit, gift increases by 2.1663
#The mailsyear coefficient in the multiple regression is smaller than the 
#mailsyear coefficient in the simple regression

#Question 9(iii) 
#Holding mailsyear and giftlast constant, if proresp increases by one percent, 
#gift increases by 15.3586

#Question 9(iV)
m9_3 = ols('gift ~ mailsyear + giftlast + propresp + avggift', data=df9).fit() 
m9_3.summary()
#The coefficient of mailsyear increases to 1.2012

#Question 9(V)
#The coefficient of giftlast deacreases to -0.2609 (and becomes negative)
#This is likely because avggift was an important omitted variable and that the 
#coefficients of the other independent variables were inflated prior to adding
#avggift because of the omitted variable bias

#Question 11
df11 = pd.read_csv('MEAPSINGLE.csv')
df11.head()
df11.describe()

df11.isnull().sum()

#Question 11(i)
m11_1 = ols('math4 ~ pctsgle', data=df11).fit() 
m11_1.summary()
#math4 = 96.7704 - 0.8329*pctsgle 
#R-Squared = 0.380
#Sample Size = 229
#Yes somewhat, for every one percent increase in single parents, math scores    
#drop by 0.8329% (NOT 83.29%) (That's almost a 1:1 negative relationship)

#Question 11(ii)
m11_2 = ols('math4 ~ pctsgle + lmedinc + free', data=df11).fit() 
m11_2.summary()
#math4 = 51.7232 - 0.1996*pctsgle + 3.5601*lmedinc - 0.3964*free
#The coefficient for pctsgle increased to -0.1996 (increases b/c its a smaller
#negative)
#This is likely because pctsgle was previously inflated (without lmedinc and
#free) due to an omitted variable bias

#Question 11(iii)
pearsonr(df11.lmedinc,df11.free)
#The correlation coefficient = -0.7469703472294885 w/ a p-value = 4.055270550593039e-42
#The negative correlation was expected, because an increase in median income 
#means more income, while an increase in free lunch eligibility means a decrease
#income

#Question 11(vi)
#No. because lmedinc captures the actual income (as a percent). while free
#captures those under an income threshold (usually poverty level)

#Question 11(v) 

variables2 = m11_2.model.exog
vif2 = [variance_inflation_factor(variables2, i) for i in range(variables2.shape[1])]
vif2 
#The coefficient with the highest VIF is pctsgle at 5.74
#This indicates a moderate correlation with other independent variables, but it
#is still well below 10, meaning its tolerable. 