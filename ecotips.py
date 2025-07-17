import streamlit as st
import requests

def render_eco_tips():
    st.subheader("🌞 Eco Tips Generator")

    keyword = st.text_input("Enter topic (e.g., plastic, solar, energy)")

    if st.button("Generate Tips"):
        try:
            response = requests.get(f"http://127.0.0.1:8000/get-eco-tips?keyword={keyword}")
            tips = response.json().get("tips", "No tips found")
            st.info("🌿 " + tips)
        except:
            st.error("🚫 Backend not reachable")
