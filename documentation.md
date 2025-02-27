# RunTracker Documentation

## Overview
RunTracker is a Strava-like application built with Streamlit that allows users to track their running activities, visualize progress, and maintain an activity log.

## Technical Stack Breakdown

### Core Technologies
1. **Python (3.11)**
   - Primary programming language
   - Used for data processing, analysis, and backend logic
   - Chosen for its rich ecosystem of data science libraries

2. **Streamlit**
   - Modern web framework for data applications
   - Provides interactive widgets and data visualization tools
   - Enables rapid development of data-driven interfaces
   - Handles state management and UI updates automatically

### Data Processing & Analysis
1. **Pandas**
   - Data manipulation and analysis library
   - Handles CSV file operations efficiently
   - Provides DataFrame structure for activity data
   - Used for statistical calculations and data transformations

2. **NumPy**
   - Numerical computing library
   - Supports advanced mathematical operations
   - Used for array operations and calculations
   - Powers the statistical analysis features

### Visualization Libraries
1. **Plotly**
   - Interactive plotting library
   - Creates dynamic and responsive charts
   - Supports various chart types (line, bar, pie)
   - Used for trend analysis and data visualization

### Storage
- **CSV-based local storage**
  - Simple, portable data storage solution
  - Easy to backup and version control
  - Structured data format for activities

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

#### Analytics (components/analytics.py)
- Advanced performance metrics:
  - Pace trends over time
  - Activity type analysis
  - Monthly progress tracking
  - Personal records tracking

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
- date: Activity date (YYYY-MM-DD)
- activity_type: Type of running activity
- distance: Distance in kilometers
- duration: Duration in minutes
- pace: Calculated pace in min/km
- calories: Estimated calories burned
- notes: User notes/comments

## Implementation Details

### Data Processing
- Activity data is processed using Pandas DataFrames
- Statistical calculations utilize NumPy for efficiency
- Real-time metrics updates on new activity logs

### Visualization Implementation
- Plotly Express for quick, attractive charts
- Plotly Graph Objects for custom visualizations
- Interactive charts with zoom and hover details

### State Management
- Streamlit session state for persistent data
- Automatic UI updates on data changes
- Efficient data caching for performance

## Setup Instructions
1. Install required packages:
   ```bash
   pip install streamlit pandas plotly numpy
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
│   ├── analytics.py     # Advanced analytics
│   ├── activity_logger.py    # Activity logging
│   └── activity_history.py   # Activity history
├── data_manager.py      # Data management
├── utils.py            # Utility functions
└── main.py            # Main application
```

## Future Enhancements
1. Advanced analytics and insights
   - Machine learning for performance predictions
   - Advanced trend analysis
   - Personalized recommendations
2. Personal records and achievements
   - Automatic milestone detection
   - Achievement badges
   - Progress tracking