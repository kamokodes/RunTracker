import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import numpy as np

def calculate_trends(df):
    """Calculate performance trends from activity data."""
    if df.empty:
        return None
    
    df['date'] = pd.to_datetime(df['date'])
    df['week'] = df['date'].dt.isocalendar().week
    df['month'] = df['date'].dt.month
    
    # Calculate rolling averages
    df['rolling_pace'] = df['pace'].rolling(window=3, min_periods=1).mean()
    df['rolling_distance'] = df['distance'].rolling(window=3, min_periods=1).mean()
    
    return df

def render_analytics(data_manager):
    st.header("📊 Advanced Analytics")
    
    # Get activity data
    df = data_manager.get_activities()
    if df.empty:
        st.info("Start logging your activities to see advanced analytics!")
        return
        
    df = calculate_trends(df)
    
    # Performance Trends
    st.subheader("🎯 Performance Trends")
    col1, col2 = st.columns(2)
    
    with col1:
        # Pace Trend
        fig_pace = px.line(df, x='date', y='rolling_pace',
                          title='Pace Trend (3-activity rolling average)',
                          labels={'rolling_pace': 'Pace (min/km)', 'date': 'Date'})
        st.plotly_chart(fig_pace, use_container_width=True)
        
    with col2:
        # Distance Trend
        fig_distance = px.line(df, x='date', y='rolling_distance',
                             title='Distance Trend (3-activity rolling average)',
                             labels={'rolling_distance': 'Distance (km)', 'date': 'Date'})
        st.plotly_chart(fig_distance, use_container_width=True)
    
    # Activity Type Analysis
    st.subheader("🏃‍♂️ Activity Type Analysis")
    activity_stats = df.groupby('activity_type').agg({
        'distance': ['mean', 'max', 'count'],
        'pace': 'mean',
        'duration': 'mean'
    }).round(2)
    
    activity_stats.columns = ['Avg Distance', 'Max Distance', 'Count', 'Avg Pace', 'Avg Duration']
    st.dataframe(activity_stats)
    
    # Monthly Progress
    st.subheader("📅 Monthly Progress")
    monthly_stats = df.groupby('month').agg({
        'distance': 'sum',
        'duration': 'sum',
        'calories': 'sum'
    }).round(2)
    
    fig_monthly = go.Figure()
    fig_monthly.add_trace(go.Bar(
        x=monthly_stats.index,
        y=monthly_stats['distance'],
        name='Total Distance (km)'
    ))
    fig_monthly.update_layout(title='Monthly Distance Progress')
    st.plotly_chart(fig_monthly, use_container_width=True)
    
    # Personal Records
    st.subheader("🏆 Personal Records")
    records = {
        'Longest Run': f"{df['distance'].max():.2f} km",
        'Fastest Pace': f"{df['pace'].min():.2f} min/km",
        'Most Calories Burned': f"{df['calories'].max():.0f} cal",
        'Longest Duration': f"{df['duration'].max():.0f} min"
    }
    
    col1, col2, col3, col4 = st.columns(4)
    cols = [col1, col2, col3, col4]
    
    for (title, value), col in zip(records.items(), cols):
        with col:
            st.metric(title, value)
