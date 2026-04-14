<<<<<<< HEAD
=======
# AI_Exposure_index

# This feature analyses how different jobs are impacted by AI using two feautres:
# -AI Exposure Index
# -Automation Probability

# The feature performs the following:
# Rank jobs by AI Exposure Index
# Compare Exposure with Automation Probability
# Identifies jobs with high exposure but low automation



# import libraries
# pandas load and filter the CSV data

>>>>>>> ecc4d9235e1389b74a33bb5b606dc7fcea71ab2d
import pandas as pd

#----------------------------------------------
# Section 1: Data preparation
#----------------------------------------------
def prepare_data(data):
    """
    Select only the columns needed for AI Exposure Analysis
    """
    return data[["Job_Title", "AI_Exposure_Index", "Automation_Probability_2030"]]


#-----------------------------------------------
# Section 2: Rank Jobs by AI Exposure Index
#-----------------------------------------------
def rank_jobs_by_exposure(feature_data):
    """
    Returns top 10 jobs with highest AI exposure
    """
    sorted_data = feature_data.sort_values(by="AI_Exposure_Index", ascending=False)
    return sorted_data.head(10)


#------------------------------------------------
# Section 3: Compare Exposure with Automation Probability
#------------------------------------------------
def compare_exposure_with_automation(feature_data):
<<<<<<< HEAD
    """
    Returns all jobs sorted by AI Exposure for comparison
    """
    return feature_data.sort_values(by="AI_Exposure_Index", ascending=False)


#------------------------------------------------
# Section 4: Identify High Risk Jobs
#------------------------------------------------
def identify_high_risk_jobs(feature_data):
    """
    Jobs with high exposure AND high automation probability
    """
    high_exposure = feature_data["AI_Exposure_Index"] > 0.7
    high_automation = feature_data["Automation_Probability_2030"] > 0.7

    return feature_data[high_exposure & high_automation]


#------------------------------------------------
# Section 5: Identify Low Risk Jobs 
#------------------------------------------------
def identify_low_risk_jobs(feature_data):
    """
    Jobs with low exposure AND low automation probability
    """
    low_exposure = feature_data["AI_Exposure_Index"] < 0.3
    low_automation = feature_data["Automation_Probability_2030"] < 0.3

    return feature_data[low_exposure & low_automation]


#------------------------------------------------
# Section 6: Simple CLI UI
#------------------------------------------------
def display_menu():
    print("\n=== AI Exposure Analysis ===")
    print("1. Show Top 10 Jobs by AI Exposure")
    print("2. Compare Exposure with Automation")
    print("3. Show High Risk Jobs")
    print("4. Show Low Risk Jobs")
    print("5. Exit")


def run_ui(feature_data):
    """
    Simple text-based UI for user interaction
    """
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
            print("\nHigh Risk Jobs:\n")
            print(identify_high_risk_jobs(feature_data))

        elif choice == "4":
            print("\nLow Risk Jobs:\n")
            print(identify_low_risk_jobs(feature_data))

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")


#------------------------------------------------
def run_ai_exposure_index(data):
    """
    Entry point for this feature
    Pass in your full dataset from main project
    """
    feature_data = prepare_data(data)
    run_ui(feature_data)
=======
    # I will select the columns needed for comparision
    comparision_data=feature_data[["Job_Title","AI_Exposure_Index","Automation_Probability_2030"]]
    # I will sort the data again by AI Exposure for a clear comparision
    comparision_data=comparision_data.sort_values(by="AI_Exposure_Index", ascending=False)
    return comparision_data

#-------------------------------------------------
# Section 4: Identify High Exposure and low Automation Jobs
#-------------------------------------------------
# This section identifies jobs with High Exposure and low Automation
# The Purpose of this section is to find jobs that are strongly affected by AI
# while still being less likely to be fully automated

def high_exposure_low_automation(feature_data):
    # Here I will calculate the average values
    average_exposure=feature_data["AI_Exposure_Index"].mean()
    average_automation=feature_data["Automation_Probability_2030"].mean()

    # Filter jobs with High Exposure but low Automation
    filtered_jobs=feature_data[
    (feature_data["AI_Exposure_Index"] > average_exposure) & (feature_data["Automation_Probability_2030"] < average_automation)
    ]
    return filtered_jobs

>>>>>>> ecc4d9235e1389b74a33bb5b606dc7fcea71ab2d






