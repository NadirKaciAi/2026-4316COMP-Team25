# AI_Exposure_index

# This feature analyses how different jobs are impacted by AI using two feautres:
# -AI Exposure Index
# -Automation Probability

# The feature performs the following:
# Rank jobs by AI Exposure Index
# Compare Exposure with Automation Probability
# Identifies jobs with high exposure but low automation



#import libraries
# pandas loads and filters the CSV data

import pandas as pd

#----------------------------------------------
# Section 1: Data preparation
#----------------------------------------------
#Select only the columns needed for Ai Exposure Analysis
def prepare_data(data):
    Feature_data=data[["Job_Title","AI_Exposure_Index","Automation_Probability_2030"]]
    return Feature_data






