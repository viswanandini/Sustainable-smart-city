# app/services/anomaly_detector.py
import pandas as pd

def detect_anomalies(data: pd.DataFrame, target_column: str, threshold: float = 2.0):
    anomalies = []
    mean = data[target_column].mean()
    std = data[target_column].std()

    for idx, value in enumerate(data[target_column]):
        z_score = (value - mean) / std if std != 0 else 0
        if abs(z_score) > threshold:
            anomalies.append({"index": idx, "value": value, "z_score": round(z_score, 2)})

    return anomalies