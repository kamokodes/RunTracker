import streamlit as st
from datetime import datetime

def render_activity_logger(data_manager):
    st.header("📝 Log Activity")
    
    with st.form("activity_form"):
        date = st.date_input("Date", datetime.now())
        
        activity_type = st.selectbox(
            "Activity Type",
            ["Running", "Jogging", "Trail Running", "Track Running"]
        )
        
        col1, col2 = st.columns(2)
        with col1:
            distance = st.number_input("Distance (km)", 
                                     min_value=0.0, 
                                     max_value=1000.0, 
                                     step=0.1)
        with col2:
            duration = st.number_input("Duration (minutes)", 
                                     min_value=0, 
                                     max_value=1440, 
                                     step=1)
        
        notes = st.text_area("Notes", placeholder="How was your run?")
        
        submitted = st.form_submit_button("Save Activity")
        
        if submitted:
            activity_data = {
                'date': date.strftime('%Y-%m-%d'),
                'activity_type': activity_type,
                'distance': distance,
                'duration': duration,
                'notes': notes
            }
            
            data_manager.save_activity(activity_data)
            st.success("Activity saved successfully!")
            st.balloons()
