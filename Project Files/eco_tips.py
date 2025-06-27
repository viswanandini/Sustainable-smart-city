import streamlit as st
import requests

# Function to get eco tips from FastAPI
def fetch_eco_tips(keyword):
    try:
        response = requests.post(
            "http://127.0.0.1:8000/get-eco-tips",
            json={"keyword": keyword},
            timeout=10
        )
        if response.status_code == 200:
            return response.json().get("tips", "No tips found.")
        else:
            return f"⚠️ Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"❌ Server error: {str(e)}"

# Streamlit UI for eco tips
def eco_tips_ui():
    st.markdown("### 🌱 Eco Advice Generator")
    st.write("Get sustainable living tips based on a topic like plastic, water, solar, recycling, etc.")

    keyword = st.text_input("Enter a keyword (e.g., plastic, energy, water):", key="eco_keyword")

    if st.button("Generate Tips", use_container_width=True):
        if keyword.strip():
            with st.spinner("Generating eco-friendly advice..."):
                tips = fetch_eco_tips(keyword.strip())
            st.success("Here are your tips:")
            st.markdown(f"📝 {tips}")
        else:
            st.warning("Please enter a keyword.")
