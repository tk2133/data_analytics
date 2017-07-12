#coding:utf-8
import numpy as np
import statsmodels.api as sm
import pandas as pd
import csv
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('./dataset_senkyo.csv')
win_list = []
len(win_list)
with open('./win_list.tsv', 'r') as f:
    reader = csv.reader(f, delimiter = '\t')
    for name in reader:
        win_list.append(name[0])
df['win'] = 0
for i in range(len(df)):
    if df.loc[i,'name'] in win_list:
        df.loc[i,'win'] = 1
    else:
        df.loc[i,'win'] = 0
X = df.drop('win',1)
Y = df['win']
Y.sum()
dummy_df = pd.get_dummies(X[['area','affiliation', 'recommend', 'status']], drop_first = True)
dummy_df
df2 = pd.merge(X, dummy_df, left_index=True, right_index=True)
X = df2.drop(['area', 'carrer','affiliation', 'recommend', 'status','name'],1)
X
#skelearn
model = LogisticRegression()
result = model.fit(X,Y)
result.coef_
# logit_mod = sm.Logit(spector_data.endog, spector_data.exog)
glm_model = sm.GLM(Y, X, family=sm.families.Binomial())
# logit_res = logit_mod.fit(disp=0)
glm_reslt = glm_model.fit(method='bfgs')
# Logit Model
logit_mod = sm.Logit(Y.values, X.values)
logit_mod
result = logit_mod.fit(method='bfgs')
result.summary()
result.summary()
result.predict(spector_data.exog)
