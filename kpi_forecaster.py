# app/services/kpi_forecaster.py
import pandas as pd
from sklearn.linear_model import LinearRegression

def forecast_kpi(data: pd.DataFrame, target_column: str, periods: int = 12):
    model = LinearRegression()
    data = data.reset_index(drop=True)
    data['time'] = range(len(data))

    X = data[['time']]
    y = data[target_column]

    model.fit(X, y)

    future_times = pd.DataFrame({'time': range(len(data), len(data) + periods)})
    forecast = model.predict(future_times)

    return list(forecast)
