#coding:utf-8
from scipy.stats import poisson
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

#ポアソン分布に従う乱数発生 size固定
arr1 = np.random.poisson(lam = 1, size = 1000)
arr2 = np.random.poisson(lam = 4, size = 1000)
arr3 = np.random.poisson(lam = 10, size = 1000)

# plot
plt.hist(arr1, label='$\lambda$=1', bins=20, range = (0,20), alpha = 0.5, color='blue')
plt.hist(arr2, bins=20, label='$\lambda$=4', range = (0,20), alpha = 0.5, color='red')
plt.hist(arr3, label = '$\lambda$=10', bins=20, range = (0,20), alpha = 0.5, color='green')
plt.legend()

#ポアソン分布に従う乱数発生 lam固定
arr1 = np.random.poisson(lam = 4, size = 100)
arr2 = np.random.poisson(lam = 4, size = 1000)
arr3 = np.random.poisson(lam = 4, size = 10000)

# plot
plt.hist(arr1, label='size=100', bins=20, range = (0,20), alpha = 0.5, color='blue')
plt.hist(arr2, bins=20, label='size=1000', range = (0,20), alpha = 0.5, color='red')
plt.hist(arr3, label = 'size=10000', bins=20, range = (0,20), alpha = 0.5, color='green')
plt.legend()

# 平均は10です。
mu = 10

# 平均と分散を計算できます。
mean,var = poisson.stats(mu)

# 確率質量関数を使って、特定の確率を計算することも可能です。
from scipy.stats import poisson
lam = 3
poisson.pmf(4,lam)*100

1 - poisson.cdf(4, lam)
