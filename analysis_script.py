import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Define file paths
DATA_PATH = r"c:\Users\sanja\OneDrive\Desktop\Regulatory Affairs of Road Accident Data 2020 India\Regulatory Affairs of Road Accident Data 2020 India.csv"
OUTPUT_DIR = os.path.dirname(DATA_PATH)

def analyze_data():
    print("Loading data...")
    try:
        df = pd.read_csv(DATA_PATH)
    except FileNotFoundError:
        print(f"Error: File not found at {DATA_PATH}")
        return

    print("\n--- Key Insights ---")
    
    # Total stats
    total_accidents = df[df['Outcome of Incident'] == 'Total number of Accidents']['Count'].sum()
    total_fatalities = df[df['Outcome of Incident'] == 'Persons Killed']['Count'].sum()
    print(f"Total Accidents: {int(total_accidents)}")
    print(f"Total Fatalities: {int(total_fatalities)}")

    # City stats
    city_accidents = df[df['Outcome of Incident'] == 'Total number of Accidents'].groupby('Million Plus Cities')['Count'].sum().sort_values(ascending=False)
    print(f"City with most accidents: {city_accidents.index[0]} ({int(city_accidents.iloc[0])})")

    city_fatalities = df[df['Outcome of Incident'] == 'Persons Killed'].groupby('Million Plus Cities')['Count'].sum().sort_values(ascending=False)
    print(f"City with most fatalities: {city_fatalities.index[0]} ({int(city_fatalities.iloc[0])})")

    # Visualizations
    sns.set_style("whitegrid")
    
    # 1. Top 10 Cities by Accidents
    plt.figure(figsize=(12, 6))
    sns.barplot(x=city_accidents.head(10).values, y=city_accidents.head(10).index, palette="viridis")
    plt.title("Top 10 Cities with Highest Road Accidents (2020)")
    plt.xlabel("Number of Accidents")
    plt.ylabel("City")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "top_10_cities_accidents.png"))
    plt.close()

    # 2. Top 10 Cities by Fatalities
    plt.figure(figsize=(12, 6))
    sns.barplot(x=city_fatalities.head(10).values, y=city_fatalities.head(10).index, palette="magma")
    plt.title("Top 10 Cities with Highest Road Fatalities (2020)")
    plt.xlabel("Number of Fatalities")
    plt.ylabel("City")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "top_10_cities_fatalities.png"))
    plt.close()

    # 3. Accident Causes Distribution
    # Check for Cause categories
    cause_accidents = df[df['Outcome of Incident'] == 'Total number of Accidents'].groupby('Cause category')['Count'].sum().sort_values(ascending=False)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=cause_accidents.values, y=cause_accidents.index, palette="coolwarm")
    plt.title("Distribution of Accidents by Cause Category")
    plt.xlabel("Number of Accidents")
    plt.ylabel("Cause Category")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "accident_causes_distribution.png"))
    plt.close()

    # 4. Traffic Control Analysis
    # Filter for Traffic Control category specifically if it exists, or just use the subcategory analysis if 'Traffic Control' is the main category for these.
    # Based on file view, 'Traffic Control' is a value in 'Cause category'.
    traffic_control_df = df[df['Cause category'] == 'Traffic Control']
    
    if not traffic_control_df.empty:
        outcomes_by_control = traffic_control_df[traffic_control_df['Outcome of Incident'].isin(['Persons Killed', 'Total Injured'])]
        outcomes_by_control = outcomes_by_control.groupby(['Cause Subcategory', 'Outcome of Incident'])['Count'].sum().unstack()
        
        outcomes_by_control.plot(kind='bar', figsize=(12, 6), stacked=True)
        plt.title("Accident Outcomes by Traffic Control Type")
        plt.xlabel("Traffic Control Type")
        plt.ylabel("Count")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(os.path.join(OUTPUT_DIR, "outcome_by_control_type.png"))
        plt.close()

    print("Analysis complete. Images saved to:", OUTPUT_DIR)

if __name__ == "__main__":
    analyze_data()
