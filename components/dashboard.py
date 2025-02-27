import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import pandas as pd

def render_dashboard(data_manager):
    st.header("🏃‍♂️ Dashboard")
    
    # Display header image
    st.image("https://images.unsplash.com/photo-1623340172826-5720529e3ce7", 
             use_column_width=True, 
             caption="Stay motivated, keep running!")

    # Get statistics
    stats = data_manager.get_stats()
    
    # Display key metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Distance", f"{stats['total_distance']} km")
    with col2:
        st.metric("Activities", stats['total_activities'])
    with col3:
        st.metric("Total Duration", f"{stats['total_duration']} mins")
    with col4:
        st.metric("Avg Pace", f"{stats['avg_pace']} min/km")

    # Get activities data
    df = data_manager.get_activities()
    if not df.empty:
        df['date'] = pd.to_datetime(df['date'])
        
        # Weekly distance chart
        st.subheader("Weekly Distance")
        weekly_distance = df.resample('W', on='date')['distance'].sum().reset_index()
        fig_weekly = px.bar(weekly_distance, x='date', y='distance',
                           labels={'date': 'Week', 'distance': 'Distance (km)'},
                           color_discrete_sequence=['#FF4B4B'])
        st.plotly_chart(fig_weekly, use_container_width=True)

        # Activity type distribution
        st.subheader("Activity Distribution")
        activity_dist = df['activity_type'].value_counts()
        fig_dist = px.pie(values=activity_dist.values, 
                         names=activity_dist.index,
                         color_discrete_sequence=px.colors.qualitative.Set3)
        st.plotly_chart(fig_dist, use_container_width=True)
    else:
        st.info("Start logging your activities to see your progress!")
