#coding:utf-8
import pandas as pd
import numpy as np

#データフレーム内の値に対応した他の値の
# python データフレームで検索
df = pd.DataFrame(np.random.randn(5,3), columns=['a','b','c'])
a_list = df['a'].tolist()
b_list = df['b'].tolist()

dict_ab = {}
for i, j in zip(a_list, b_list):
    print(i)
    dict_ab[i,j] = np.random.randn(1)[0]
dict_ab

def mapping_ab(a,b):
    return dict_ab[a,b]

df['ab'] = df.apply(lambda x: mapping_ab(x['a'],x['b']),axis=1)
df

dict_a = {}
for i,n in enumerate(df['a']):
    dict_a[n] = i

df['mapped_a'] = df['a'].map(dict_a)

def pri(x):
    return print(x)

df.apply(lambda x: pri(x[0]))
df.applymap(dict_a)


a = np.array([[2,4],[4,2]])
np.linalg.eig(a)
import statsmodels.formula.api as smf
X = df.drop('ab',axis=1)
Y = df['ab']
model = smf.OLS(Y,X)
result = model.fit()
result.summary()

A=X.as_matrix()
np.dot(np.linalg.inv(np.dot(A.transpose(),A)),A.transpose())
