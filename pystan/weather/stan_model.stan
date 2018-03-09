data {
  int<lower=0> N;
  //int Y[N];
  vector[N] Y;
  vector[N] weather_temperature;
  vector[N] weather_wind;
}

parameters {
  vector[N] cold_resistance;
  real<lower=0> s_cold;
  real weather_temperature_par;
  real weather_wind_par;
  real<lower=0> s_mu;
}

transformed parameters {
  vector[N] y_mean;
  y_mean = weather_temperature_par * weather_temperature + weather_wind_par * weather_wind + cold_resistance;
}

model {
  cold_resistance[3:N] ~ normal(2*cold_resistance[2:(N-1)] - cold_resistance[1:(N-2)], s_cold);
  //cold_resistance[2:N] ~ normal(cold_resistance[1:(N-1)], s_cold);
  //Y ~ normal(y_mean, s_mu);
  for(i in 1:N)
    Y[i] ~ poisson_log(y_mean[i]);
  Y ~ poisson_log(y_mean);
}
