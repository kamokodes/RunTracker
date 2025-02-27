# Import required libraries and components
import streamlit as st
from data_manager import DataManager
from components.dashboard import render_dashboard
from components.activity_logger import render_activity_logger
from components.activity_history import render_activity_history
from components.analytics import render_analytics
from utils import load_css, initialize_session_state

# Configure the Streamlit page settings
st.set_page_config(
    page_title="RunTracker",  # Set browser tab title
    page_icon="🏃‍♂️",        # Set browser tab icon
    layout="wide"           # Use wide layout for better visualization
)

# Initialize application components
load_css()                 # Load custom styling
initialize_session_state() # Set up session state for data persistence
data_manager = DataManager()  # Initialize data management system

# Create sidebar navigation
st.sidebar.title("RunTracker")
# Add motivational image to sidebar
st.sidebar.image(
    "https://images.unsplash.com/photo-1518644961665-ed172691aaa1",
    use_container_width=True
)

# Navigation menu using radio buttons
navigation = st.sidebar.radio(
    "Go to",
    ["Dashboard", "Analytics", "Log Activity", "Activity History"]
)

# Route to appropriate component based on navigation selection
if navigation == "Dashboard":
    render_dashboard(data_manager)  # Show main dashboard
elif navigation == "Analytics":
    render_analytics(data_manager)  # Show advanced analytics
elif navigation == "Log Activity":
    render_activity_logger(data_manager)  # Show activity logging form
else:
    render_activity_history(data_manager)  # Show activity history

# Add footer
st.sidebar.markdown("---")
st.sidebar.markdown("Made with ❤️ for runners")