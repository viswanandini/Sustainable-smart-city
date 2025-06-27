import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import requests
import os
import sys

# Ensure root path is in sys.path (if needed for internal imports)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Optional PDF report generator (if implemented)
try:
    from app.services.generate_report import generate_pdf_report
    REPORT_ENABLED = True
except ImportError:
    REPORT_ENABLED = False

# Streamlit UI Configuration
st.set_page_config(page_title="📈 Smart City Forecast Dashboard", layout="wide")

st.title("📊 Smart City KPI Forecast & Anomaly Dashboard")
st.markdown("Upload your city's KPI CSV file and run forecasting or anomaly detection.")

# Upload CSV
uploaded_file = st.file_uploader("📂 Upload City KPI CSV", type=["csv"])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("✅ File uploaded successfully.")
        st.dataframe(df.head())

        # Column selection
        target_col = st.selectbox("📊 Select a column to forecast or analyze", df.columns)

        # Forecast
        if st.button("🔮 Forecast"):
            with st.spinner("Forecasting in progress..."):
                response = requests.post(
                    "http://localhost:8000/forecast/kpi",
                    files={"file": uploaded_file.getvalue()},
                    data={"target_column": target_col}
                )
                if response.status_code == 200:
                    forecast_data = pd.DataFrame(response.json())
                    st.success("✅ Forecast generated!")
                    st.line_chart(forecast_data)
                else:
                    st.error(f"❌ Forecasting failed: {response.text}")

        # Anomaly Detection
        if st.button("🚨 Detect Anomalies"):
            with st.spinner("Detecting anomalies..."):
                response = requests.post(
                    "http://localhost:8000/forecast/anomaly",
                    files={"file": uploaded_file.getvalue()},
                    data={"target_column": target_col}
                )
                if response.status_code == 200:
                    anomaly_df = pd.DataFrame(response.json())
                    st.success("✅ Anomalies detected!")

                    fig, ax = plt.subplots()
                    sns.lineplot(data=anomaly_df, x="date", y="value", ax=ax, label="KPI")
                    anomalies = anomaly_df[anomaly_df["anomaly"] == True]
                    sns.scatterplot(data=anomalies, x="date", y="value", color="red", label="Anomaly", ax=ax)

                    plt.xticks(rotation=45)
                    plt.tight_layout()
                    st.pyplot(fig)
                else:
                    st.error(f"❌ Anomaly detection failed: {response.text}")

        # Optional: Generate PDF report
        if REPORT_ENABLED and st.button("📄 Download PDF Report"):
            with st.spinner("Generating report..."):
                pdf_path = generate_pdf_report(df, target_col)
                with open(pdf_path, "rb") as f:
                    st.download_button(
                        label="📥 Download Report",
                        data=f,
                        file_name="smart_city_report.pdf",
                        mime="application/pdf"
                    )

    except Exception as e:
        st.error(f"❌ Error processing file: {e}")
else:
    st.info("⬆️ Please upload a KPI CSV file to begin.")
