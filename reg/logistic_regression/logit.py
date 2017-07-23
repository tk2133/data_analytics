#coding:utf-8
import numpy as np
import statsmodels.api as sm
import pandas as pd
import csv
import os
from sklearn.linear_model import LogisticRegression
import seaborn as sns
from matplotlib import pyplot as plt
%matplotlib inline

path = '/users/takahiro-nakano/github_personal/regression/logistic_regression/'

import pandas as pd
import csv
#説明変数のデータをimport
df = pd.read_csv(path + 'dataset_senkyo.csv')

#目的変数のデータをimport
win_list = []
with open(path + 'win_list.tsv', 'r') as f:
    reader = csv.reader(f, delimiter = '\t')
    for name in reader:
        win_list.append(name[0])



#説明変数のデータフレームに目的変数を追加
for i in range(len(df)):
    if df.loc[i,'name'] in win_list:
        df.loc[i,'win'] = 1
    else:
        df.loc[i,'win'] = 0
df.head()
#相関行列の計算
corr = np.corrcoef(X.transpose())
names = X.columns.values
sns.heatmap(corr, annot=True,
                xticklabels=names,
                yticklabels=names)


#説明変数、目的変数
X = df.drop('win',1)
Y = df['win']

#ダミー変数作成
dummy_df = pd.get_dummies(X[['affiliation', 'status']], drop_first = True)
df2 = pd.merge(X, dummy_df, left_index=True, right_index=True)
X = df2.drop(['area', 'carrer','affiliation', 'recommend', 'status','name','teisu','number'],1)
X.head()
#skelearn
model = LogisticRegression()
result = model.fit(X,Y)
result.coef_
# logit_mod = sm.Logit(spector_data.endog, spector_data.exog)
glm_model = sm.GLM(Y, X, family=sm.families.Binomial())
# logit_res = logit_mod.fit(disp=0)
glm_reslt = glm_model.fit(method='bfgs')
# Logit Model
import statsmodels.api as sm
logit = sm.Logit(Y, X)
logit
result = logit.fit()
result.summary2()
df
import math
math.exp(6.1328)
math.exp(-0.03)
math.exp(2.19)
