import sys
import os
import streamlit as st

# Fix ModuleNotFoundError by adding project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'frontend')))

# Add 'frontend' directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'frontend')))

# Import UI components
from frontend.components.chat_assistant import chat_assistant_ui
from frontend.components.eco_tips import eco_tips_ui
from frontend.components.feedback_form import feedback_form_ui
from frontend.components.summary_card import summary_card_ui
from frontend.components.report_generator import report_generator_ui
from components.forecasting_dashboard import forecasting_dashboard_ui

# Streamlit app setup
st.set_page_config(
    page_title="Sustainable Smart City Assistant",
    layout="wide",
    page_icon="🌱"
)

# Sidebar navigation
st.sidebar.title("🌍 Smart City Dashboard")
page = st.sidebar.radio("Choose a section", [
    "📊 Summary Dashboard",
    "🤖 Chat Assistant",
    "💡 Eco Tips",
    "📝 Feedback Form",
    "📄 Generate Report"
])

# Routing based on selected section
if page == "📊 Summary Dashboard":
    summary_card_ui()

elif page == "🤖 Chat Assistant":
    chat_assistant_ui()

elif page == "💡 Eco Tips":
    eco_tips_ui()

elif page == "📝 Feedback Form":
    feedback_form_ui()

elif page == "📄 Generate Report":
    report_generator_ui()

# Footer
st.markdown("---")
st.markdown("© 2025 Smart City Initiative | Built with ❤️ using Streamlit")

