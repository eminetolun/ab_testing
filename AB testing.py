

# Import Packages

import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.stats.api as sms
from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind, mannwhitneyu, pearsonr, spearmanr, kendalltau, \
    f_oneway, kruskal
from statsmodels.stats.proportion import proportions_ztest

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

## Variables

#Impression : Number of ad views
#Click : Click
#Purchase: Indicates the number of products purchased after the clicked ads.
#Earning : Earnings after purchased items


# Read Excel
trainSet = pd.read_excel(".../data.xlsx", sheet_name="Control Group")
testSet = pd.read_excel(".../data.xlsx", sheet_name="Test Group")


trainSet.isnull().sum()
testSet.isnull().sum()

len(trainSet)
len(testSet)
trainSet.columns
############################
# 1. Assumption Check
############################

# Normality Assumption
# Variance Homogeneity

############################
# Normality Assumption
############################

#H0: There is no difference between the number of products purchased. (p-value < 0.05)
#H1: Normal distribution assumption not provided.


test_stat, pvalue = shapiro(trainSet["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# Test Stat = 0.9773, p-value = 0.5891


test_stat, pvalue = shapiro(testSet["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# Test Stat = 0.9589, p-value = 0.1541

# Fail to reject H0. Normal Distribution .

############################
# Variance Homogeneity
############################

#H0: Variances are Homogeneous
#H1: Variances Are Not Homogeneous

test_stat, pvalue  = levene(trainSet["Purchase"], testSet["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# Fail to reject H0. Variances are Homogeneous.


# H0 : M1 =  M2 (A/B groups are similar.)
# H1 : M1 !=  M2 (A/B groups are not similar.)

test_stat , pvalue = ttest_ind(trainSet["Purchase"],testSet["Purchase"] )
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# Fail to reject H0.A/B groups are similar.


