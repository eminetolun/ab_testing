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

## DEĞİŞKENLER

#Impression : Reklam görüntüleme sayısı
#Click
#Purchase:Satın Alım
#Earning : Kazanç



trainSet = pd.read_excel(".../data.xlsx", sheet_name="Control Group")
testSet = pd.read_excel(".../data.xlsx", sheet_name="Test Group")


trainSet.isnull().sum()
testSet.isnull().sum()

len(trainSet)
len(testSet)
trainSet.columns
############################
# 1. Varsayım Kontrolü
############################

# Normallik Varsayımı
# Varyans Homojenliği

############################
# Normallik Varsayımı
############################

# H0: Normal dağılım varsayımı sağlanmaktadır.
# H1: Normal dağılım varsayımı sağlanmamaktadır.

test_stat, pvalue = shapiro(trainSet["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# Test Stat = 0.9773, p-value = 0.5891


test_stat, pvalue = shapiro(testSet["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# Test Stat = 0.9589, p-value = 0.1541

# İki veri seti için shapiro testi p value değeri > 0,05'ten büyük olduğu için  normal dağılımı varsayımı sağlanmaktadır. H0 reddedilemez.
#İkinci varsayım olan varyans homojenliği varsayımı kontrol edilir.

############################
# Varyans Homojenligi Varsayımı
############################

# H0: Varyanslar Homojendir
# H1: Varyanslar Homojen Değildir


test_stat, pvalue  = levene(trainSet["Purchase"], testSet["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# H0 reddedilemez. İki örneklem arasındaki varyanslar homojendir.
# Varsayımlar sağlandığı için bağımsız iki örneklem t testine geçilebilir.


#HİPOTEZLER
# H0 : M1 =  M2 (İki grup ortalamaları arasında istatistiksel olarak anlamlı bir fark yoktur.)
# H1 : M1 !=  M2 (İki grup ortalamaları arasında istatistiksel olarak anlamlı bir fark vardır.)

test_stat , pvalue = ttest_ind(trainSet["Purchase"],testSet["Purchase"] )
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# pvalue > 0,05 olduğu için H0 reddedilemez. İki grup arasında istatistiksel olarak anlamlı bir fark yoktur.
# Mevcut teklif verme türünü kullanmaya devam etmelidir.



