# Road Accident Analysis - India (2020) 🇮🇳 🚦

This project analyzes road accident data from Million Plus Cities in India for the year 2020. Using Python, it explores patterns regarding accident frequencies, fatalities, causes, and traffic control measures to derive actionable insights.

## 📂 Dataset
The dataset contains regulatory affairs data regarding road accidents in India (2020).
- **Download the Data:** [Google Drive Link](https://drive.google.com/file/d/1ft84zICATQqhB1egy4DQJs4bIckcA-0f/view?usp=sharing)
- **Format:** CSV

## 📊 Key Insights & Visualizations
The script generates the following insights based on the data:

1.  **Highest Accident Rate:** **Chennai** recorded the highest number of road accidents (~26,000+).
2.  **Highest Fatalities:** **Delhi** recorded the highest number of fatalities (~7,000+), despite having fewer total accidents than Chennai.
3.  **Traffic Control:** A significant portion of accidents occurred in "Uncontrolled" areas or areas classified as "Others," indicating a need for better traffic management infrastructure.
4.  **Leading Causes:** The majority of accidents were categorized under "Impacting Vehicle/Object" and "Junction" related incidents.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Libraries:**
    * `pandas` (Data Manipulation)
    * `matplotlib` (Plotting)
    * `seaborn` (Statistical Visualization)

## 🚀 How to Run

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    ```

2.  **Install dependencies:**
    ```bash
    pip install pandas matplotlib seaborn
    ```

3.  **Configure Data Path:**
    * Open `analysis_script.py`.
    * Update the `DATA_PATH` variable on **Line 7** to point to the location where you saved the CSV file on your machine.
    ```python
    # Example
    DATA_PATH = "path/to/your/Regulatory Affairs of Road Accident Data 2020 India.csv"
    ```

4.  **Run the script:**
    ```bash
    python analysis_script.py
    ```

## 📈 Generated Outputs
The script automatically saves the following charts to your local directory:
* `top_10_cities_accidents.png`
* `top_10_cities_fatalities.png`
* `accident_causes_distribution.png`
* `outcome_by_control_type.png`

## 🤝 Contributing
Feel free to fork this repository and submit pull requests to improve the analysis or add new visualizations.
