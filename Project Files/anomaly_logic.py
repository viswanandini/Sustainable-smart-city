# backend/anomaly_logic.py
import matplotlib.pyplot as plt

def run_anomaly_detection(df):
    column = df.select_dtypes(include='number').columns[0]
    ts = df[column]

    mean = ts.mean()
    std = ts.std()
    anomalies = ts[(ts < mean - 2*std) | (ts > mean + 2*std)]

    fig, ax = plt.subplots(figsize=(10, 4))
    ts.plot(ax=ax, label="Data")
    ax.scatter(anomalies.index, anomalies, color='red', label='Anomalies')
    ax.set_title("Anomaly Detection")
    ax.legend()
    return fig
