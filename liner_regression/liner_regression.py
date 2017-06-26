#coding:utf-8
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from sklearn.datasets import load_boston
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.graphics.regressionplots as regplot
%matplotlib inline

#ボストン価格データのインポート
boston = load_boston()
df = pd.DataFrame(boston.data, columns=boston.feature_names)
#住宅価格のデータをデータフレームに追加する
df['Price'] = boston.target
#先頭5行の表示
df.head()
#記述統計量
df.describe()
#データセットの詳細
print(boston.DESCR)

#plot
#散布図
sns.jointplot('RM', 'Price', data=df)
#全変数間の散布図
sns.pairplot(df, kind = "reg")

#OLS
#Xに説明変数,Yに目的変数のデータを格納
X = df.drop('Price',1)
Y = boston.target
model = smf.OLS(Y,X)
result = model.fit()
result.summary()

#残差PLOT　第二引数で変数の指定
regplot.plot_regress_exog(result,0)

#RMとDISの交差項の追加
X['RM_DIS'] = X['RM'] * X['RAD']
model = smf.OLS(Y,X)
result = model.fit()
result.summary()

#plot
sns.pairplot(df, kind = "reg", vars=['Price','RM','DIS'])
