import pandas as pd
import os
from datetime import datetime

class DataManager:
    def __init__(self):
        self.activities_file = "activities.csv"
        self.create_activities_file()

    def create_activities_file(self):
        if not os.path.exists(self.activities_file):
            df = pd.DataFrame(columns=[
                'date', 'activity_type', 'distance', 'duration',
                'pace', 'calories', 'notes'
            ])
            df.to_csv(self.activities_file, index=False)

    def save_activity(self, activity_data):
        df = pd.read_csv(self.activities_file)
        activity_data['pace'] = round(activity_data['duration'] / activity_data['distance'], 2) if activity_data['distance'] > 0 else 0
        activity_data['calories'] = round(activity_data['distance'] * 60)  # Simple calorie calculation
        df = pd.concat([df, pd.DataFrame([activity_data])], ignore_index=True)
        df.to_csv(self.activities_file, index=False)

    def get_activities(self):
        if os.path.exists(self.activities_file):
            return pd.read_csv(self.activities_file)
        return pd.DataFrame()

    def get_stats(self):
        df = self.get_activities()
        if df.empty:
            return {
                'total_distance': 0,
                'total_activities': 0,
                'total_duration': 0,
                'avg_pace': 0
            }
        
        return {
            'total_distance': round(df['distance'].sum(), 2),
            'total_activities': len(df),
            'total_duration': round(df['duration'].sum(), 2),
            'avg_pace': round(df['duration'].sum() / df['distance'].sum(), 2) if df['distance'].sum() > 0 else 0
        }
