import streamlit as st
from reportlab.pdfgen import canvas
from io import BytesIO
from datetime import datetime

def generate_ai_summary(city, kpi_text):
    return f"""
    📊 Sustainability Report for {city.title()}

    🔍 Based on KPIs:
    {kpi_text.strip()}

    📋 Insights:
    - {city.title()} is making progress on key metrics.
    - Efficient use of water and energy is observed.
    - AQI is within healthy range but needs constant monitoring.

    ✅ Recommendations:
    - Promote renewable energy (solar, wind).
    - Encourage public transport and green spaces.
    - Monitor waste disposal and recycling efforts.

    📅 Generated on: {datetime.now().strftime("%Y-%m-%d %H:%M")}
    """

def create_pdf(summary_text):
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer)
    pdf.setFont("Helvetica", 12)

    y = 800
    for line in summary_text.split('\n'):
        pdf.drawString(50, y, line.strip())
        y -= 20
        if y < 50:
            pdf.showPage()
            y = 800
    pdf.save()
    buffer.seek(0)
    return buffer

def report_generator_ui():
    st.subheader("📥 City Sustainability Report Generator")
    st.markdown("Generate AI-powered reports based on city name and recent KPIs")

    city = st.text_input("Enter City Name")
    kpi_text = st.text_area("Paste recent KPI summary (e.g., water usage, energy, etc.)")

    if st.button("🧠 Generate Report"):
        if not city or not kpi_text:
            st.error("Please fill in both city name and KPI summary.")
            return

        with st.spinner("Generating your report..."):
            summary = generate_ai_summary(city, kpi_text)
            st.text_area("📝 AI-Generated Summary", summary.strip(), height=300)

            pdf = create_pdf(summary)
            st.download_button(
                label="📄 Download PDF Report",
                data=pdf,
                file_name=f"{city}_Report.pdf",
                mime="application/pdf"
            )
