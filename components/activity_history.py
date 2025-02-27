import streamlit as st
import pandas as pd

def render_activity_history(data_manager):
    st.header("📅 Activity History")
    
    df = data_manager.get_activities()
    if not df.empty:
        df['date'] = pd.to_datetime(df['date'])
        df = df.sort_values('date', ascending=False)
        
        for _, activity in df.iterrows():
            with st.container():
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    st.subheader(f"{activity['activity_type']} on {activity['date'].strftime('%B %d, %Y')}")
                    st.write(f"📏 Distance: {activity['distance']} km")
                    st.write(f"⏱️ Duration: {activity['duration']} minutes")
                    st.write(f"⚡ Pace: {activity['pace']} min/km")
                    
                with col2:
                    st.write(f"🔥 Calories: {activity['calories']}")
                    if activity['notes']:
                        st.write(f"📝 Notes: {activity['notes']}")
                
                st.divider()
    else:
        st.info("No activities logged yet. Start tracking your runs!")
