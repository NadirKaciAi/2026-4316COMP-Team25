# ---------------------------------------------------------
# skill_analysis.py
#
# This file handles all skill-related analysis for the project.
# It allows the user to:
# 1. Find jobs that require a minimum level of a chosen skill
# 2. View the full skill profile of a chosen job
#
# The file can run on its own for testing but will later be imported into
# main.py during final touches.
# ---------------------------------------------------------

def run_skill_analysis(data):
    """
    Main function for skill analysis.
    This is called from main.py if the user selects this feature.
    """

    # Clean job titles (prevents matching errors)
    data["Job_Title"] = data["Job_Title"].astype(str).str.strip()

    # Display menu
    print("\nSkill Analysis")
    print("-------------------")
    print("1 - Find jobs by skill level")
    print("2 - View skill profile of a job")

    # Get user choice
    choice = input("Select an option (1 or 2): ").strip()


# Import libraries
# os is used to build the file path to the dataset
# pandas is used to load and filter the CSV data
import os
import pandas as pd


# ---------------------------------------------------------
# Check whether the user's chosen skill number is valid
# The dataset only contains Skill_1 to Skill_10
# ---------------------------------------------------------
def validate_skill_number(skill_number):
    return 1 <= skill_number <= 10


# ---------------------------------------------------------
# Convert a skill number into the correct dataset column name
# Example: 3 becomes "Skill_3"
# ---------------------------------------------------------
def get_skill_column(skill_number):
    return f"Skill_{skill_number}"


# ---------------------------------------------------------
# Filter all jobs where the selected skill is at least
# the minimum level entered by the user
# ---------------------------------------------------------
def filter_jobs_by_skill(data, skill_number, min_level):
    skill_column = get_skill_column(skill_number)

    # Use pandas boolean filtering to return only matching rows
    filtered_jobs = data[data[skill_column] >= min_level]

    return filtered_jobs


# ---------------------------------------------------------
# Return a sorted list of unique job titles that match
# the selected skill and minimum level
# ---------------------------------------------------------
def get_jobs_by_skill(data, skill_number, min_level):
    filtered_jobs = filter_jobs_by_skill(data, skill_number, min_level)

    # If no jobs match, return an empty list
    if filtered_jobs.empty:
        return []

    # Remove missing values, remove duplicates, convert to a list, then sort
    jobs = filtered_jobs["Job_Title"].dropna().unique().tolist()
    jobs.sort()

    return jobs


# ---------------------------------------------------------
# Return the top matching jobs based on the selected skill value
# Jobs with the highest score in the chosen skill appear first
# ---------------------------------------------------------
def get_top_matching_jobs(data, skill_number, min_level, top_n=10):
    filtered_jobs = filter_jobs_by_skill(data, skill_number, min_level)

    # If nothing matched, return an empty DataFrame
    if filtered_jobs.empty:
        return pd.DataFrame()

    skill_column = get_skill_column(skill_number)

    # Sort by the selected skill column in descending order
    top_jobs = filtered_jobs.sort_values(
        by=skill_column,
        ascending=False
    )[["Job_Title", skill_column]].head(top_n)

    return top_jobs

# ---------------------------------------------------------
# Return the full skill profile for a job title
# So if the user types part of the job title, it can still work
# For example: "data" could match "Data Scientist"
# ---------------------------------------------------------
def get_skill_profile_by_job(data, job_title):
    # Find all jobs whose title contains the user's input text
    job_matches = data[
        data["Job_Title"].str.lower().str.contains(job_title.lower(), na=False)
    ]

    # If no matches are found, return nothing
    if job_matches.empty:
        return None

    # Select the first matching row
    job_row = job_matches.iloc[0]

    # Store all 10 skill values
    skills = {}
    for i in range(1, 11):
        skills[f"Skill_{i}"] = job_row[f"Skill_{i}"]

    # Return the job title and the skill profile
    return {
        "job_title": job_row["Job_Title"],
        "skills": skills
    }

    