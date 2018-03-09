#coding:utf-8
import numpy as np
import statsmodels.api as sm
import pandas as pd
import csv
import os


path = 'ファイルの置いてあるpath'

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

#説明変数、目的変数
X = df.drop('win',1)
Y = df['win']

#ダミー変数作成
dummy_df = pd.get_dummies(X[['affiliation', 'status']], drop_first = True)
df2 = pd.merge(X, dummy_df, left_index=True, right_index=True)
X = df2.drop(['area', 'carrer','affiliation', 'recommend', 'status','name','teisu','number'],1)

#modeling
logit = sm.Logit(Y, X)
result = logit.fit(method = 'bfgs')
result.summary2()
