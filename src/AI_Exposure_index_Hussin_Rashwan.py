# AI_Exposure_index

# This feature analyses how different jobs are impacted by AI using two feautres:
# -AI Exposure Index
# -Automation Probability

# The feature performs the following:
# Rank jobs by AI Exposure Index
# Compare Exposure with Automation Probability
# Identifies jobs with high exposure but low automation



# import libraries
# pandas loads and filters the CSV data

import pandas as pd

#----------------------------------------------
# Section 1: Data preparation
#----------------------------------------------
# Select only the columns needed for AI Exposure Analysis
def prepare_data(data):
    feature_data=data[["Job_Title","AI_Exposure_Index","Automation_Probability_2030"]]
    return feature_data


#-----------------------------------------------
#  Section 2: Rank Jobs by AI Exposure Index
#-----------------------------------------------
def rank_jobs_by_exposure(feature_data):
    # Sort jobs by AI Exposure Index in descending order
    sorted_data=feature_data.sort_values(by="AI_Exposure_Index", ascending=False)

    # I will get the top 10 jobs with highest AI Exposure
    top_jobs=sorted_data.head(10)
    return top_jobs

#------------------------------------------------
# Section 3: Compare Exposure with Automation probability
#------------------------------------------------
def compare_exposure_with_automation(feature_data):
    # I will select the columns needed for comparision
    comparision_data=feature_data[["Job_Title","AI_Exposure_Index","Automation_Probability_2030"]]
    # I will sort the data again by AI Exposure for a clear comparision
    comparision_data=comparision_data.sort_values(by="AI_Exposure_Index", ascending=False)
    return comparision_data







