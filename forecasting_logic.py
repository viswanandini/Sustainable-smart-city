# backend/forecasting_logic.py
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

def run_forecasting(df):
    # Use the first numeric column (or replace with a specific one like 'energy')
    column = df.select_dtypes(include='number').columns[0]
    ts = df[column]

    result = seasonal_decompose(ts, model='additive', period=7)

    fig, ax = plt.subplots(4, 1, figsize=(10, 8))
    result.observed.plot(ax=ax[0], title='Observed')
    result.trend.plot(ax=ax[1], title='Trend')
    result.seasonal.plot(ax=ax[2], title='Seasonal')
    result.resid.plot(ax=ax[3], title='Residual')

    plt.tight_layout()
    return fig
