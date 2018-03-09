#coding:utf-8
import numpy as np
import pandas as pd
import statsmodels.api as sm

#データのインポート
df = pd.read_csv("http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/rhc.csv")
df.head()

# データの整形
df = df.iloc[:,1:]
df1 = df[['cat1','sex','death','age','swang1','meanbp1','aps1']]
df1.head()

#クロス集計
pd.crosstab(df.death,df.swang1)

#傾向スコアを求めるのに使う説明変数
X = df1.drop(['death','swang1'],1)
dummy_X = pd.get_dummies(X[['cat1','sex']],drop_first=True)
X2 = pd.merge(X, dummy_X, left_index=True, right_index=True)
X = X2.drop(['cat1','sex'],1)


#施術したかどうかダミー変数化
ps_target = df1['swang1']
dummy_ps = pd.get_dummies(ps_target)
ps_target = dummy_ps['RHC']

#death ダミー変数化
y = df1['death']
dummy_y = pd.get_dummies(y)
y = dummy_y['Yes']

"""
#説明変数
X = df.drop(['death','swang1'],1)
dummy_X = pd.get_dummies(X[['cat1','cat2','ca','sex','dth30','dnr1','ninsclas','resp','card','neuro','gastr','renal','meta',
                            'hema','seps','trauma','ortho','race','income']],drop_first=True)
X2 = pd.merge(X, dummy_X, left_index=True, right_index=True)
X = X2.drop(['cat1','cat2','ca','sex','dth30','dnr1','ninsclas','resp','card','neuro','gastr','renal','meta',
                            'hema','seps','trauma','ortho','race','income'],1)
"""


#傾向スコアを求める
glm = sm.Logit(ps_target, X)
result = glm.fit()
result.summary2()
ps.head()

#IPW推定量
ps = pd.Series(result.predict(X))
z1 = ps_target
y = y
ipwe1 = sum((z1*y)/ps)/sum(z1/ps)
ipwe0 = sum(((1-z1)*y)/(1-ps))/sum((1-z1)/(1-ps))
ipwe1
ipwe0
ipwe1 - ipwe0

#Propensity score matching
table = pd.concat([ps,z1,y],axis=1)
table.columns = ['ps','treat','died']

interval = np.arange(0,1.05,0.05)
match_list = []
for i in range(0,len(interval)-1):
    temp0 = table[(table['treat']==0) & (interval[i] < table['ps']) & (table['ps'] < interval[i+1])]
    temp1 = table[(table['treat']==1) & (interval[i] < table['ps']) & (table['ps'] < interval[i+1])]
    if (len(temp0) > 0) & (len(temp1) > 0):
        match_list.append(temp1['died'].mean()-temp0['died'].mean())

np.mean(match_list)
