# app/services/forecasting_service.py

import pandas as pd
from statsmodels.tsa.seasonal import STL
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from datetime import datetime, timedelta

def forecast_kpi(df, column='value', periods=7):
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    df = df.asfreq('D')  # daily frequency
    df[column] = df[column].interpolate()

    model = ExponentialSmoothing(df[column], trend='add', seasonal='add', seasonal_periods=7)
    fitted_model = model.fit()

    forecast = fitted_model.forecast(periods)
    forecast_df = forecast.reset_index().rename(columns={0: 'forecast', 'index': 'date'})
    return forecast_df

def detect_anomalies(df, column='value'):
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    df[column] = df[column].interpolate()

    stl = STL(df[column], seasonal=7)
    result = stl.fit()
    resid = result.resid

    threshold = resid.std() * 2
    df['anomaly'] = (abs(resid) > threshold).astype(int)
    return df.reset_index()
