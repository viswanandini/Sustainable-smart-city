import streamlit as st
from streamlit.components.v1 import html

def summary_card_ui(data: dict):
    """
    Render summary cards for key sustainability metrics.
    
    Parameters:
    - data (dict): Dictionary with keys like 'Pollution', 'Temperature', 'Water Quality', etc.
    """

    st.subheader("🌍 City Sustainability Summary")
    st.markdown("---")

    cols = st.columns(len(data))

    for i, (metric, value) in enumerate(data.items()):
        with cols[i]:
            st.metric(label=metric, value=value)
