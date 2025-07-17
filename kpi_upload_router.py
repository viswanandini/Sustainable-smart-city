# app/api/kpi_upload_router.py
from fastapi import APIRouter, UploadFile, File
import pandas as pd
import io
from app.services.kpi_forecaster import forecast_kpi
from app.services.anomaly_detector import detect_anomalies

router = APIRouter()

@router.post("/kpi/upload")
async def process_kpi(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    target_column = df.columns[-1]  # assuming last column is target

    forecast = forecast_kpi(df, target_column)
    anomalies = detect_anomalies(df, target_column)

    return {
        "target": target_column,
        "forecast": forecast,
        "anomalies": anomalies
    }
