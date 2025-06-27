import streamlit as st
import requests

def render_feedback():
    st.subheader("📝 Citizen Feedback Form")

    category = st.selectbox("Issue Category", ["Water", "Electricity", "Sanitation", "Road", "Other"])
    description = st.text_area("Describe the issue in detail")

    if st.button("Submit Report"):
        try:
            payload = {
                "category": category,
                "description": description
            }
            response = requests.post("http://127.0.0.1:8000/submit-feedback", json=payload)
            if response.status_code == 200:
                st.success("✅ Feedback submitted!")
            else:
                st.error("❌ Failed to submit feedback.")
        except:
            st.error("🚫 Cannot connect to backend.")