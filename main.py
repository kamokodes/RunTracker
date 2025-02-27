import streamlit as st
from data_manager import DataManager
from components.dashboard import render_dashboard
from components.activity_logger import render_activity_logger
from components.activity_history import render_activity_history
from components.analytics import render_analytics
from utils import load_css, initialize_session_state

# Page config
st.set_page_config(
    page_title="RunTracker",
    page_icon="🏃‍♂️",
    layout="wide"
)

# Initialize
load_css()
initialize_session_state()
data_manager = DataManager()

# Sidebar navigation
st.sidebar.title("RunTracker")
st.sidebar.image("https://images.unsplash.com/photo-1518644961665-ed172691aaa1", use_container_width=True)

navigation = st.sidebar.radio(
    "Go to",
    ["Dashboard", "Analytics", "Log Activity", "Activity History"]
)

# Main content
if navigation == "Dashboard":
    render_dashboard(data_manager)
elif navigation == "Analytics":
    render_analytics(data_manager)
elif navigation == "Log Activity":
    render_activity_logger(data_manager)
else:
    render_activity_history(data_manager)

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("Made with ❤️ for runners")