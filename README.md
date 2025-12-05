# Road Accident Data Analysis (India 2020)

## Project Overview
This project analyzes the "Regulatory Affairs of Road Accident Data 2020 India" dataset to identify key trends and insights regarding road accidents in major Indian cities. The analysis focuses on understanding the distribution of accidents across cities, the primary causes of accidents, and the impact of different traffic control measures.

## Dataset
The dataset contains information about road accidents in Million Plus Cities in India for the year 2020. Key columns include:
- **Million Plus Cities**: Name of the city.
- **Cause category**: Broad category of the accident cause (e.g., Traffic Control).
- **Cause Subcategory**: Specific cause (e.g., Traffic Light Signal, Over Speeding).
- **Outcome of Incident**: Consequence (e.g., Persons Killed, Total Injured).
- **Count**: Number of incidents/persons.

## Key Analysis & Insights
The Python script `analysis_script.py` performs the following analysis:
1.  **City-wise Trends**: Identifies top cities with the highest number of accidents and fatalities.
2.  **Cause Analysis**: Visualizes the distribution of accidents by cause category.
3.  **Traffic Control Impact**: Examines accident outcomes based on different traffic control mechanisms (e.g., Traffic Lights, Police Controlled).

### Visualizations Generated
- `top_10_cities_accidents.png`: Bar chart of top 10 cities by total accidents.
- `top_10_cities_fatalities.png`: Bar chart of top 10 cities by total fatalities.
- `accident_causes_distribution.png`: Distribution of accidents across different cause categories.
- `outcome_by_control_type.png`: Stacked bar chart showing injuries and fatalities for different traffic control types.

## How to Run
1.  Ensure you have Python installed with the following libraries:
    ```bash
    pip install pandas matplotlib seaborn
    ```
2.  Run the analysis script:
    ```bash
    python analysis_script.py
    ```
3.  The script will print key statistics to the console and save the visualization images in the same directory.
