library(rstan)
library(dplyr)

weather_data = read.csv("data_weather.csv", header = F)
trend_data = read.csv("google_trend.csv", header = F)

data_length = weather_data %>% nrow
weather_temperature = weather_data[,2]
weather_wind = weather_data[,3]
google_trend = trend_data[,2]

dat = list(N = data_length,Y = google_trend,
           weather_temperature = weather_temperature,
           weather_wind = weather_wind)

fit = stan(file = 'stan_model.stan', data = dat, iter = 2000, chains = 4)
a = summary(fit)$summary[,"mean"]
plot(a[1:182])
stan_trace(fit, pars = "weather_temperature_par")
stan_trace(fit, pars = "weather_wind_par")

################################################
################################################
################################################
fit2 = stan(file = 'stan_model2.stan', data = dat, iter = 500, chains = 2)

