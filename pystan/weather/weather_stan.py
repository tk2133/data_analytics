#coding:utf-8
from pystan import StanModel
import pandas as pd

weather_data = pd.read_csv('~/github_personal/pystan/weather/data/data_weather.csv',names=['temp','wind'])
trend_data = pd.read_csv('~/github_personal/pystan/weather/data/google_trend.csv',names=['trend'])

data_length = len(weather_data)
weather_temperature = weather_data['temp']
weather_wind = weather_data['wind']
google_trend = trend_data['trend']

data = {'N':data_length,
        'Y':google_trend,
        'weather_temperature':weather_temperature,
        'weather_wind':weather_wind}

stanmodel = StanModel(file='/Users/takahiro-nakano/github_personal/pystan/weather/stan_model.stan')
fit_nuts = stanmodel.sampling(data=data, n_jobs=1, iter=100, chains = 4)
print(fit_nuts.summary())
mcmc_sample = fit_nuts.extract()
a = mcmc_sample['a']
b = np.array([i for i in range(len(a))])
fit_nuts.plot()
plt.show()
