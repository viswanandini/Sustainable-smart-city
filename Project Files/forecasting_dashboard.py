# frontend/components/forecasting_dashboard.py
import streamlit as st
import pandas as pd
from backend.forecasting_logic import run_forecasting
from backend.anomaly_logic import run_anomaly_detection

def forecasting_dashboard_ui():
    st.subheader("📈 Forecast & Detect Anomalies from City Metrics")

    uploaded_file = st.file_uploader("📤 Upload CSV file", type=["csv"])

    if uploaded_file:
        st.success("✅ File uploaded. Processing now...")
        df = pd.read_csv(uploaded_file)

        st.write("📝 Uploaded Data Preview", df.head())

        # 🔮 Forecasting
        st.markdown("### 🔮 Forecasting Visualization")
        forecast_fig = run_forecasting(df)
        st.pyplot(forecast_fig)

        # 🚨 Anomaly Detection
        st.markdown("### 🚨 Anomaly Detection")
        anomaly_fig = run_anomaly_detection(df)
        st.pyplot(anomaly_fig)
