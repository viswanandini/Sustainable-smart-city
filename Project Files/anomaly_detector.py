import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import zscore

def detect_anomalies_zscore(data, threshold=3):
    """
    Detect anomalies in a time series using Z-score method.
    """
    df = data.copy()
    df['zscore'] = zscore(df['value'])
    df['anomaly'] = df['zscore'].abs() > threshold
    return df

def anomaly_detector_ui():
    st.subheader("📉 Anomaly Detection Dashboard")

    uploaded_file = st.file_uploader("Upload CSV File (with 'value' column)", type=['csv'])
    
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)

            if 'value' not in df.columns:
                st.error("The CSV must contain a 'value' column.")
                return

            st.write("### Raw Data")
            st.dataframe(df.head())

            threshold = st.slider("Z-Score Threshold", min_value=1.0, max_value=5.0, value=3.0, step=0.1)

            result_df = detect_anomalies_zscore(df, threshold)

            st.write("### Detected Anomalies")
            st.dataframe(result_df[result_df['anomaly']])

            # Plot
            st.write("### Anomaly Plot")
            plt.figure(figsize=(10, 5))
            sns.lineplot(data=result_df, x=result_df.index, y="value", label="Value")
            sns.scatterplot(data=result_df[result_df['anomaly']], x=result_df[result_df['anomaly']].index, y="value", color="red", label="Anomaly")
            plt.xlabel("Index")
            plt.ylabel("Value")
            plt.title("Anomaly Detection")
            st.pyplot(plt)

        except Exception as e:
            st.error(f"Error reading file: {e}")
    else:
        st.info("Please upload a CSV file to detect anomalies.")
