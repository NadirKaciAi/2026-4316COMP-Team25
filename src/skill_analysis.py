# ---------------------------------------------------------
# skill_analysis.py
#
# This file handles all skill-related analysis for the project.
# It allows the user to:
# 1. Find jobs by skill level and view its AI exposure
# 2. View the full skill profile of a chosen job and its AI exposure
# ---------------------------------------------------------

import pandas as pd

# main function to run the skill analysis menu and handle user choices
def run_skill_analysis(data):
    data["Job_Title"] = data["Job_Title"].astype(str).str.strip()

    print("\nSkill Analysis")
    print("1. Find jobs by skill level and view AI exposure")
    print("2. View a job's skill profile and AI exposure")

    choice = input("Choose an option: ").strip()

# user inputs and then it is validated that the skill number is between 1 and 10
 if choice == "1":
        try:
            skill_number = int(input("Enter skill number (1-10): "))
            min_level = float(input("Enter minimum level (0-1): "))
        except ValueError:
            print("Invalid input.")
            return

        # basic validation before we do anything
        if not valid_skill_number(skill_number):
            print("Skill number must be between 1 and 10.")
            return
        if min_level < 0 or min_level > 1:
            print("Minimum level must be between 0 and 1.")
            return

# variables
jobs = jobs_by_skill(data, skill_number, min_level)
avg_exposure = average_ai_exposure_by_skill(data, skill_number, min_level)
top_jobs = top_jobs_by_skill(data, skill_number, min_level)

