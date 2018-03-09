#coding:utf-8
import numpy as np
from sklearn import datasets
from matplotlib import pyplot as plt
import matplotlib
import seaborn as sns
%matplotlib inline

sns.factorplot(x='survived',y='sex',data=df)

g = sns.FacetGrid(titanic, col="sex",  row="class")
g = g.map(plt.hist, "age")
df = titanic.dropna()
sns.pairplot(data=df)
titanic = sns.load_dataset('titanic')
titanic.head()

current_pallette = sns.color_palette(n_colors=23)
sns.palplot(current_pallette)

plt.figure(figsize=(18,10))
plt.subplot(121)
sns.countplot('age',data=titanic)

plt.subplot(122)
sns.countplot('sex', data=titanic)


sns.countplot(x='class',hue='sex', data=titanic, palette=sns.color_palette("RdBu"))
plt.xlabel('AAA')
#sample data
X = [1,2,3]
Y = np.array([3,6,4])
label = ['A','B','C']


plt.hist(np.array(titanic['age']))
#基本形
plt.bar(X,Y)

#目盛りを変更
plt.bar(X,Y,tick_label=label)

plt.bar(X,Y)
plt.xticks(X,label)
plt.xlabel('品種')
plt.ylabel('高さ')

#色を変える
color_dict = matplotlib.colors.cnames
color_dict
plt.bar(X,Y,tick_label=label,color=color_dict['red'], width=0.8, edgecolor =color_dict['blue'], linewidth=3)



#積み上げ棒

#横棒表示
