from fastapi import APIRouter, UploadFile, File, Form
import pandas as pd
import io
from app.services.forecasting_service import forecast_kpi, detect_anomalies

router = APIRouter(prefix="/forecast", tags=["Forecasting"])

@router.post("/kpi")
async def forecast(file: UploadFile = File(...), target_column: str = Form(...)):
    contents = await file.read()
    df = pd.read_csv(io.BytesIO(contents))

    try:
        forecast_df = forecast_kpi(df, target_column)
        return forecast_df.to_dict(orient="records")
    except Exception as e:
        return {"error": str(e)}

@router.post("/anomaly")
async def anomaly(file: UploadFile = File(...), target_column: str = Form(...)):
    contents = await file.read()
    df = pd.read_csv(io.BytesIO(contents))

    try:
        anomaly_df = detect_anomalies(df, target_column)
        return anomaly_df.to_dict(orient="records")
    except Exception as e:
        return {"error": str(e)}
