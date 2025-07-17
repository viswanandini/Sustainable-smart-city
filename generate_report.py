# app/services/generate_report.py

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import os

def save_plot(df: pd.DataFrame, chart_path: str, title: str = "KPI Chart"):
    plt.figure(figsize=(10, 4))
    plt.plot(df['date'], df['value'], label="KPI")
    if 'anomaly' in df.columns:
        anomalies = df[df['anomaly'] == True]
        plt.scatter(anomalies['date'], anomalies['value'], color='red', label="Anomalies")

    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()

def generate_pdf_report(df: pd.DataFrame, filename: str = "kpi_report.pdf", title: str = "KPI Forecast Report"):
    chart_path = "chart.png"
    save_plot(df, chart_path, title)

    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(30, height - 50, title)

    # Timestamp
    c.setFont("Helvetica", 10)
    c.drawString(30, height - 70, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Chart
    c.drawImage(chart_path, 30, height - 400, width=500, preserveAspectRatio=True)

    # Summary
    c.setFont("Helvetica-Bold", 12)
    c.drawString(30, height - 420, "Summary Stats:")

    c.setFont("Helvetica", 10)
    stats = df['value'].describe()
    y = height - 440
    for i, (stat, value) in enumerate(stats.items()):
        c.drawString(40, y - (i * 15), f"{stat.capitalize()}: {round(value, 2)}")

    # Anomaly Count
    if 'anomaly' in df.columns:
        anomaly_count = df['anomaly'].sum()
        c.drawString(40, y - (len(stats) * 15) - 10, f"Anomalies Detected: {anomaly_count}")

    c.showPage()
    c.save()

    # Clean up
    if os.path.exists(chart_path):
        os.remove(chart_path)

    return filename
