# ---------------------------------------------------------
# AI_Exposure_index_Hussin_Rashwan.py
#
# This file handles all AI exposure analysis for the project.
# The user can either:
# 1. View the top 10 jobs ranked by AI Exposure Index
# 2. Compare AI exposure with automation probability
# 3. Identify high risk jobs (high exposure AND high automation)
# 4. Identify low risk jobs (low exposure AND low automation)
# ---------------------------------------------------------

# Import Data Loader and pandas
import pandas as pd
from data_loader_Aymen import DataLoader
loader = DataLoader()
data_raw = loader.load_data()


# If a job title appears more than once, average its numeric columns
def average_duplicates(data):
    return data.groupby("Job_Title", as_index=False).mean(numeric_only=True)


# Select only the columns needed for AI Exposure Analysis
def prepare_data(data):
    return data[["Job_Title", "AI_Exposure_Index", "Automation_Probability_2030"]]


# Return top 10 jobs with highest AI Exposure Index
def rank_jobs_by_exposure(feature_data):
    sorted_data = feature_data.sort_values(by="AI_Exposure_Index", ascending=False)
    return sorted_data.head(10)


# Return all jobs sorted by AI Exposure Index for comparison
def compare_exposure_with_automation(feature_data):
    return feature_data.sort_values(by="AI_Exposure_Index", ascending=False)


# Return jobs where both AI exposure and automation probability are above 0.7
def identify_high_risk_jobs(feature_data):
    high_exposure = feature_data["AI_Exposure_Index"] > 0.7
    high_automation = feature_data["Automation_Probability_2030"] > 0.7
    filtered = feature_data[high_exposure & high_automation]
    return average_duplicates(filtered)


# Return jobs where both AI exposure and automation probability are below 0.3
def identify_low_risk_jobs(feature_data):
    low_exposure = feature_data["AI_Exposure_Index"] < 0.3
    low_automation = feature_data["Automation_Probability_2030"] < 0.3
    filtered = feature_data[low_exposure & low_automation]
    return average_duplicates(filtered)


# Print the menu options for the AI Exposure Analysis section
def display_menu():
    print("\n=== AI Exposure Analysis ===")
    print("1. Show Top 10 Jobs by AI Exposure")
    print("2. Compare Exposure with Automation")
    print("3. Show High Risk Jobs")
    print("4. Show Low Risk Jobs")
    print("5. Return to Main Menu")


# Main UI loop to handle user choices for AI exposure analysis
def run_ui(feature_data):
    while True:
        display_menu()
        choice = input("Select an option: ")

        if choice == "1":
            print("\nTop 10 Jobs by AI Exposure:\n")
            print(rank_jobs_by_exposure(feature_data))

        elif choice == "2":
            print("\nExposure vs Automation:\n")
            print(compare_exposure_with_automation(feature_data))

        elif choice == "3":
            print("\nHigh Risk Jobs (averaged if duplicates exist):\n")
            print(identify_high_risk_jobs(feature_data))

        elif choice == "4":
            print("\nLow Risk Jobs (averaged if duplicates exist):\n")
            print(identify_low_risk_jobs(feature_data))

        elif choice == "5":
            print("Returning to main menu...")
            return

        else:
            print("Invalid choice. Try again.")


# Main entry point — loads data, converts numeric columns, and launches the UI
def run_ai_exposure_index():
    data = pd.DataFrame(data_raw)

    data["AI_Exposure_Index"] = data["AI_Exposure_Index"].astype(float)
    data["Automation_Probability_2030"] = data["Automation_Probability_2030"].astype(float)

    feature_data = prepare_data(data)
    run_ui(feature_data)


if __name__ == "__main__":
    run_ai_exposure_index()