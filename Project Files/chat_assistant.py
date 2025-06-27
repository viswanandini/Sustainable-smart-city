import streamlit as st
import requests

# Function to call FastAPI /chat endpoint
def get_ai_response(user_message):
    try:
        response = requests.post(
            "http://127.0.0.1:8000/chat",
            json={"message": user_message},
            timeout=10
        )
        if response.status_code == 200:
            return response.json().get("response", "No reply received.")
        else:
            return f"⚠️ Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"❌ Server error: {str(e)}"

# Streamlit UI for chat assistant
def chat_assistant_ui():
    st.markdown("### 💬 Smart City Chat Assistant")
    st.write("Ask anything related to sustainability, city governance, energy, or eco-living!")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.text_input("👤 You:", key="user_input")

    if st.button("Send", use_container_width=True) and user_input.strip():
        with st.spinner("Watsonx is thinking... 🤖"):
            ai_reply = get_ai_response(user_input)
        
        # Save to history
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Assistant", ai_reply))
        st.session_state.user_input = ""

    # Display conversation
    for speaker, message in st.session_state.chat_history:
        if speaker == "You":
            st.markdown(f"🧑‍💻 **{speaker}**: {message}")
        else:
            st.markdown(f"🤖 **{speaker}**: {message}")
