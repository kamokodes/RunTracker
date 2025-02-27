import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import numpy as np

def calculate_trends(df):
    """
    Calculate performance trends from activity data.

    Args:
        df (pd.DataFrame): Activity data containing date, pace, and distance

    Returns:
        pd.DataFrame: Processed DataFrame with calculated trends
    """
    if df.empty:
        return None

    # Convert date column to datetime and extract time components
    df['date'] = pd.to_datetime(df['date'])
    df['week'] = df['date'].dt.isocalendar().week
    df['month'] = df['date'].dt.month

    # Calculate rolling averages for trend analysis
    df['rolling_pace'] = df['pace'].rolling(window=3, min_periods=1).mean()
    df['rolling_distance'] = df['distance'].rolling(window=3, min_periods=1).mean()

    return df

def render_analytics(data_manager):
    """
    Render the analytics dashboard with advanced insights.

    Args:
        data_manager (DataManager): Instance of DataManager for data access
    """
    st.header("📊 Advanced Analytics")

    # Get activity data from data manager
    df = data_manager.get_activities()
    if df.empty:
        st.info("Start logging your activities to see advanced analytics!")
        return

    # Process data for trend analysis
    df = calculate_trends(df)

    # Performance Trends Section
    st.subheader("🎯 Performance Trends")
    col1, col2 = st.columns(2)

    with col1:
        # Pace Trend visualization
        fig_pace = px.line(
            df, 
            x='date', 
            y='rolling_pace',
            title='Pace Trend (3-activity rolling average)',
            labels={'rolling_pace': 'Pace (min/km)', 'date': 'Date'}
        )
        st.plotly_chart(fig_pace, use_container_width=True)

    with col2:
        # Distance Trend visualization
        fig_distance = px.line(
            df, 
            x='date', 
            y='rolling_distance',
            title='Distance Trend (3-activity rolling average)',
            labels={'rolling_distance': 'Distance (km)', 'date': 'Date'}
        )
        st.plotly_chart(fig_distance, use_container_width=True)

    # Activity Type Analysis Section
    st.subheader("🏃‍♂️ Activity Type Analysis")
    # Calculate statistics grouped by activity type
    activity_stats = df.groupby('activity_type').agg({
        'distance': ['mean', 'max', 'count'],
        'pace': 'mean',
        'duration': 'mean'
    }).round(2)

    # Rename columns for better readability
    activity_stats.columns = ['Avg Distance', 'Max Distance', 'Count', 'Avg Pace', 'Avg Duration']
    st.dataframe(activity_stats)

    # Monthly Progress Section
    st.subheader("📅 Monthly Progress")
    # Calculate monthly statistics
    monthly_stats = df.groupby('month').agg({
        'distance': 'sum',
        'duration': 'sum',
        'calories': 'sum'
    }).round(2)

    # Create monthly progress visualization
    fig_monthly = go.Figure()
    fig_monthly.add_trace(go.Bar(
        x=monthly_stats.index,
        y=monthly_stats['distance'],
        name='Total Distance (km)'
    ))
    fig_monthly.update_layout(title='Monthly Distance Progress')
    st.plotly_chart(fig_monthly, use_container_width=True)

    # Personal Records Section
    st.subheader("🏆 Personal Records")
    records = {
        'Longest Run': f"{df['distance'].max():.2f} km",
        'Fastest Pace': f"{df['pace'].min():.2f} min/km",
        'Most Calories Burned': f"{df['calories'].max():.0f} cal",
        'Longest Duration': f"{df['duration'].max():.0f} min"
    }

    # Display personal records in columns
    col1, col2, col3, col4 = st.columns(4)
    cols = [col1, col2, col3, col4]

    for (title, value), col in zip(records.items(), cols):
        with col:
            st.metric(title, value)