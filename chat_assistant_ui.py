import streamlit as st
import requests

def chat_assistant_ui():
    st.subheader("💬 Smart City Chat Assistant")
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.text_input("Ask something about the smart city:")
    if user_input:
        response = requests.post("http://localhost:8000/chat", json={"query": user_input})
        assistant_reply = response.json().get("response", "No response")

        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Assistant", assistant_reply))

    for sender, message in st.session_state.chat_history:
        if sender == "You":
            st.markdown(f"**🧑‍💻 {sender}:** {message}")
        else:
            st.markdown(f"**🤖 {sender}:** {message}")
