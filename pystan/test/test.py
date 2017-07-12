import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from pystan import StanModel
%matplotlib inline

filepath = '/Users/takahiro-nakano/R/RStanBook/chap04/input/data-salary.txt'
df = pd.read_csv(filepath)
data = {'N':len(df),'X':df['X'].values,'Y':df['Y'].values}

stanmodel = StanModel(file='/Users/takahiro-nakano/github_personal/pystan/test/normal.stan')
fit_nuts = stanmodel.sampling(data=data, n_jobs=1, iter=100, chains = 4)
print(fit_nuts.summary())
mcmc_sample = fit_nuts.extract()
a = mcmc_sample['a']
b = np.array([i for i in range(len(a))])
fit_nuts.plot()
plt.show()
