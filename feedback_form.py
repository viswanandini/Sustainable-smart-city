import streamlit as st
import requests

def submit_feedback(name, location, category, message):
    try:
        response = requests.post(
            "http://127.0.0.1:8000/submit-feedback",
            json={
                "name": name,
                "location": location,
                "category": category,
                "message": message
            },
            timeout=10
        )
        if response.status_code == 200:
            return "✅ Feedback submitted successfully!"
        else:
            return f"⚠️ Failed to submit feedback: {response.status_code} - {response.text}"
    except Exception as e:
        return f"❌ Error: {str(e)}"

def feedback_form_ui():
    st.markdown("### 📝 Citizen Feedback Form")
    st.write("Help us improve the city by reporting an issue or giving feedback.")

    name = st.text_input("Your Name")
    location = st.text_input("Location (e.g., street name or area)")
    category = st.selectbox("Category", ["Water", "Traffic", "Sanitation", "Electricity", "Other"])
    message = st.text_area("Describe the issue or feedback")

    if st.button("Submit Feedback", use_container_width=True):
        if name and location and message:
            with st.spinner("Sending feedback..."):
                result = submit_feedback(name, location, category, message)
            st.success(result)
        else:
            st.warning("🚨 Please fill in all required fields.")
