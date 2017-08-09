#coding:utf-8
import numpy as np
import pandas as pd
import pyper as pr
import statsmodels.api as sm

df = pd.read_csv("http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/rhc.csv")
df.head()
df = df.iloc[:,1:]
#目的変数　propensity score
ps_target = df['swang1']
dummy_ps = pd.get_dummies(ps_target)
ps_target = dummy_ps['Yes']

#説明変数
X = df.drop(['death','swang1'],1)
dummy_X = pd.get_dummies(X[['']],drop_first=True)
X2 = pd.merge(X, dummy_X, left_index=True, right_index=True)
X = X2.drop([''],1)

#death 目的変数作成
y = df['death']
dummy_y = pd.get_dummies(y)
y = dummy_y['Yes']

#傾向スコアを求める
glm = sm.Logit(Y=df[''])
