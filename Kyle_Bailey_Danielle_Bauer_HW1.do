capture log close
cd "C:\Users\Kyle\Desktop\Python\DATA"
log using "Kyle_Bailey_Danielle_Bauer_HW1.txt", text replace
set linesize 255
set type double

insheet using "BWGHT.csv", comma names
mdesc

* Question 1(i)
* The most likely sign for B2 is positive if birth weights are correlated with better prenatal care, then having higher family income allows access to these resources leading to higher birth weights in turn

* Question 1(ii)
* cigs and faminc are likely to be loosely negatively correlated. Higher family income allows better medical care and education that bring awareness to the dangers of cigarette smoking. This is confirmed by a Pearson correlation coefficient of -0.17.
corr cigs faminc

* Question 1(iii)
reg bwght cigs faminc
* bwght = 116.9741 -0.4634cigs + 0.0928faminc, n = 1388, r2 = 0.03
* Regression without family income
reg bwght cigs
* bwght = 119.7719 -0.5138cigs, n = 1388, r2 = 0.023
* The regression results are certainly different, although not to a very high degree. The coefficient on cigs only changes from -0.46 to -0.51 (a one oz increase in birth is associated with ~.5 less cigarettes per day).
* Additionally, the fit of the model decreased only by 0.01 but with an r2 of less than .1 the explanatory power of the models are quite weak.

clear
insheet using "CEOSAL2.csv", comma names
mdesc

* Question 3(i)
reg lsalary lsales lmktval
* lsalary = 4.6209 + 0.1621lsales + 0.1067lmktval

* Question 3(ii)
reg lsalary lsales lmktval profits
* We cannot include profits in this model due to them being measured in millions, with the rest of the equation in log form, the coefficient is extraordinarily small and statistically insignificant as well. 
* Additionally, several firms in the dataset had negative profits (losses) such that trying to calculate lsalary will lead to it being undefined
* Given the r2 is roughly 0.30, I would say that this model does not capture most of the variation in CEO salaries as we can only explain 30% of salary variation, including more variables would help us more clearly see the effects.

* Question 3(iii)
reg lsalary lsales lmktval profits ceoten
* Holding all other factors fixed, if CEO tenure increases by 1 year, lsalary will increase by 1.17% 

* Question 3(iv)
corr lmktval profits
* The Pearson R coefficient between log(market value) and profits is 0.78, this implies strong correlation between the two variables and likely collinearity within the model. Higher profits are generally associated with higher market value so including both would be difficult to capture the individual effects without OLS estimators being biased.

clear
insheet using "ATTEND.csv", comma names
mdesc

* Question 4(i)
tabstat atndrte, stat(min max mean)
tabstat prigpa, stat(min max mean)
tabstat act, stat(min max mean)

* Question 4(ii)
reg atndrte prigpa act
* atndrte = 75.7004 + 17.2606priGPA - 1.7166ACT
* The intercept states that a student with a 0.0 GPA the previous term and a 0 ACT score will attend, on average, around 75% of their classes. I don't believe that it is useful in this case as any students who have these characteristics will likely be removed from school in a practical setting.

* Question 4(iii)
* The coefficient on priGPA makes sense as a one unit increase in GPA (1.0/4.0 scale) is responsible for a 17% increase in attendance rate, all else held equal. Students who get higher grades are far more likely to go to class more consistently.
* The coefficient on ACT was surprising, however, as its sign was negative when I expected it to be positive. Additionally, the magnitude implied for a 1 unit increase in the score (out of 36), attendance rate dropped 1.7%, all else held equal. 
* Students who perform higher on tests should generally be overall higher performing students.

* Question 4(iv)



* unsure about below but I think I'm on the right track just cant get it working _____________*

input prigpa
3.65
3.1
2.1
end

input act
20
21
26
end

predict yhat, 

* Question 4(v)

clear
insheet using "MEAP93.csv", comma names
mdesc

* Question 7(i)
reg math10 lexpend lnchprg
* math10 = -20.3607 + 6.2297lexpend - 0.3046lnchprg, n = 408, r2 = 0.180
* The sign on the lexpend I expected to be positive, as higher spending within a school per student will likely lead to higher math scores due to better quality teaching and materials.
* The sign on lnchprg I also expected to be negative, as students who are on lunch programs are far more likely to be from lower-income families in districts with much lower access to resources.

* Question 7(ii)
* It does not make sense to set the explanatory variable lexpend to 0. Setting it to 0 would be equivilant to setting expend = 1, which implies that a school is only spending $1 per student when the minimum value for expendature per student is $3332 in the dataset.
* Setting lnchprg to 0 makes more sense as it could be a very high income school district where students do not need to be on a school lunch program.
tabstat expend, stat(min)

* Question 7(iii)
reg math10 lexpend
* math10 = -69.3411 + 11.1644lexpend
* The slope coefficient on lexpend has increased from 6.2297 to 11.1644, a 0.05% increase in MEAP math scores per dollar spent on students

* Question 7(iv)
corr math10 lexpend
* Having math10 and lexpend being positively correlated makes sense to me given that access to better resources will generally allow students to perform better.

* Question 7(v)
* Because the two variables are positively correlated, having solely lexpend in a regression will yield a more pronounced spending effect because it is capturing the variation in both.

clear 
insheet using "DISCRIM.csv", comma names
mdesc

drop if missing(income, prpblck, psoda, prppov)
* Observations loaded in as strings, genereated new vars as int for analysis

* Question 8(i) 
gen prpblck1 = real(prpblck)
gen income1 = real(income)
tabstat prpblck1, stat(mean sd)
tabstat income1, stat(mean sd)
* income is in dollars & prpblck is a percentage

* Question 8(ii)
gen psoda1 = real(psoda)
reg psoda1 prpblck1 income1
* psoda = 0.9563 + 0.1150*prpblck + 0.000001603*income
* R-Squared = 0.064
* Sample Size = 401
* Holding income constant, if prpblock increases by one percent,
* psoda increases by 0.1150
* Yes, an increase in soda price of $0.11 does seem significant 
 
 * Question 8(iii)
 reg psoda1 prpblck1
* The discrimination effect (0.0649) is smaller without income

* Question 8(iv)
gen lpsoda1 = real(lpsoda)
gen lincome1 = real(lincome)
reg lpsoda1 prpblck1 lincome1
* log(psoda) = -0.7938 + 0.1216*prpblck + 0.0765*log(income)
* R-Squared = 0.068
* Sample Size = 401
* 2.43%

* Question 8(v)
gen prppov1 = real(prppov)
reg lpsoda1 prpblck1 lincome1 prppov1
* The coefficient for prpblck decreases to 0.0728

* Question 8(vi)
pwcorr lincome1 prppov1, sig star(.05)
* Corr Coeff = -0.8402068944304426 w/ p-value = 4.2371233881359175e-108
* Yes, I assumed that proportion in poverty and income would be highly, negatively correlated (the higher proportion in poverty, the lower the income)

* Question 8(vii)
reg lpsoda1 prpblck1 lincome1
vif 
* Not necessarily true, it depends on their VIF (they both have VIF < 10)

clear
insheet using "CHARITY.csv", comma names
mdesc

* Question 9(i)
reg gift mailsyear giftlast propresp
* gift = -4.5515 + 2.1663*mailsyear + 0.0059*giftlast + 15.3586*propresp
* R-Squared = 0.083
* Sample Size = 4268

reg gift mailsyear
* R=Squared decreased to 0.014

* Question 9(ii)
* In the multiple regression, holding giftlast and propresp constant, if mailsyear increases by one unit, gift increases by 2.1663
* The mailsyear coefficient in the multiple regression is smaller than the mailsyear coefficient in the simple regression

* Question 9(iii)
* Holding mailsyear and giftlast constant, if proresp increases by one percent, gift increases by 15.3586

* Question 9(iv)
reg gift mailsyear giftlast propresp avggift
* The coefficient of mailsyear increases to 1.2012

* Question 9(v)
* The coefficient of giftlast deacreases to -0.2609 (and becomes negative)
* This is likely because avggift was an important omitted variable and that the coefficients of the other independent variables were inflated prior to adding avggift because of the omitted variable bias

clear 
insheet using "MEAPSINGLE.csv", names
mdesc

* Question 11(i)
reg math4 pctsgle
* math4 = 96.7704 - 0.8329*pctsgle 
* R-Squared = 0.380
* Sample Size = 229
* Yes somewhat, for every one percent increase in single parents, math scores drop by 0.8329% (NOT 83.29%) (That's almost a 1:1 negative relationship)

* Question 11(ii)
reg math4 pctsgle lmedinc free
* math4 = 51.7232 - 0.1996*pctsgle + 3.5601*lmedinc - 0.3964*free
* The coefficient for pctsgle increased to -0.1996 (increases b/c its a smaller negative)
* This is likely because pctsgle was previously inflated (without lmedinc and free) due to an omitted variable bias

* Question 11(iii)
pwcorr lmedinc free, sig star(.05)
* The correlation coefficient = -0.7469703472294885 w/ a p-value = 4.055270550593039e-42
* The negative correlation was expected, because an increase in median income means more income, while an increase in free lunch eligibility means a decrease income

* Question 11(iv)
* No. because lmedinc captures the actual income (as a percent). while free captures those under an income threshold (usually poverty level)

* Question 11(v)
reg math4 pctsgle lmedinc free
vif
* The coefficient with the highest VIF is pctsgle at 5.74
* This indicates a moderate correlation with other independent variables, but it is still well below 10, meaning its tolerable. 







