#coding:utf-8
import numpy as np
from statsmodels.imputation import mice
import seaborn as sns

"""
#from データ解析プロセス
1,欠損値がでる種類
2,欠損値対処法の紹介
3,実例　python fancymse
　L　軽く理論の紹介
　L　データ・セットの用意
"""

#多重代入法
from statsmodels.imputation import mice

#ランダムにnanを発生
sample = sns.load_dataset('iris')
rand_list = np.random.choice(np.arange(150),10)
for row in rand_list:
    sample.loc[row,'sepal_length'] = np.nan

test = sample.drop('species',axis=1)
mice.MICEData(test)
