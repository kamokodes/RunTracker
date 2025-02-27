# RunTracker Documentation

## Overview
RunTracker is a Strava-like application built with Streamlit that allows users to track their running activities, visualize progress, and maintain an activity log.

## Technical Stack
- **Frontend Framework**: Streamlit
- **Data Visualization**: Plotly
- **Data Processing**: Pandas
- **Data Storage**: CSV-based local storage

## Component Structure

### 1. Main Application (main.py)
```python
# Handles application routing and navigation
# Sets up the page configuration and sidebar
# Initializes the data manager and loads CSS
```

### 2. Data Management (data_manager.py)
```python
# Manages activity data storage and retrieval
# Calculates statistics and metrics
# Handles data persistence using CSV
```

### 3. Components

#### Dashboard (components/dashboard.py)
- Displays key metrics:
  - Total Distance
  - Number of Activities
  - Total Duration
  - Average Pace
- Visualizations:
  - Weekly distance chart
  - Activity type distribution

#### Activity Logger (components/activity_logger.py)
- Form for logging new activities
- Fields:
  - Date
  - Activity Type
  - Distance
  - Duration
  - Notes
- Automatic calculations:
  - Pace (min/km)
  - Calories burned

#### Activity History (components/activity_history.py)
- Chronological display of activities
- Detailed view for each activity
- Shows calculated metrics

### 4. Styling (assets/style.css)
- Custom styling for components
- Responsive design
- Consistent color scheme
- Card-based layout

## Data Structure
Activities are stored in a CSV file with the following columns:
- date
- activity_type
- distance
- duration
- pace
- calories
- notes

## Key Features

### 1. Activity Tracking
- Log different types of running activities
- Automatic pace calculation
- Simple calorie estimation
- Notes for each activity

### 2. Data Visualization
- Weekly progress tracking
- Activity type distribution
- Real-time metric updates

### 3. User Interface
- Clean, intuitive design
- Responsive layout
- Easy navigation
- Visual feedback on actions

## Future Enhancements
1. Advanced analytics and insights
2. Personal records and achievements

## Setup Instructions
1. Install required packages:
   ```bash
   pip install streamlit pandas plotly
   ```
2. Run the application:
   ```bash
   streamlit run main.py
   ```

## File Organization
```
├── .streamlit/
│   └── config.toml      # Streamlit configuration
├── assets/
│   └── style.css        # Custom styling
├── components/
│   ├── dashboard.py     # Dashboard component
│   ├── activity_logger.py    # Activity logging
│   └── activity_history.py   # Activity history
├── data_manager.py      # Data management
├── utils.py            # Utility functions
└── main.py            # Main application
```
