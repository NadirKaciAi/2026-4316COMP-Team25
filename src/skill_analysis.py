# ---------------------------------------------------------
# skill_analysis.py
#
# This file handles all skill-related analysis for the project.
# The user can either:
# 1. Find jobs by skill level and view its AI exposure
# 2. View the full skill profile of a chosen job and its AI exposure
# ---------------------------------------------------------

import pandas as pd


# Main function to run the skill analysis menu and handle user choices
def run_skill_analysis(data):
    data["Job_Title"] = data["Job_Title"].astype(str).str.strip()

    print("\nSkill Analysis")
    print("1. Find jobs by skill level and view AI exposure")
    print("2. View a job's skill profile and AI exposure")

    choice = input("Choose an option: ").strip()

    # User inputs are validated so the skill number is between 1 and 10
    if choice == "1":
        try:
            skill_number = int(input("Enter skill number (1-10): "))
            min_level = float(input("Enter minimum level (0-1): "))
        except ValueError:
            print("Invalid input.")
            return

        if not valid_skill_number(skill_number):
            print("Skill number must be between 1 and 10.")
            return

        if min_level < 0 or min_level > 1:
            print("Minimum level must be between 0 and 1.")
            return

        # Run the main calculations
        jobs = jobs_by_skill(data, skill_number, min_level)
        avg_exposure = average_ai_exposure_by_skill(data, skill_number, min_level)
        top_jobs = top_jobs_by_skill(data, skill_number, min_level)

        if not jobs:
            print("No matching jobs found.")
            return

        print(f"\nJobs with Skill_{skill_number} >= {min_level}:")
        for job in jobs:
            print("-", job)

        print(f"\nTotal jobs found: {len(jobs)}")
        print(f"Average AI Exposure Index: {avg_exposure:.2f}")
        print("\nTop matches:")
        print(top_jobs.to_string(index=False))

    elif choice == "2":
        job_title = input("Enter a job title: ").strip()
        result = skill_profile_by_job(data, job_title)

        if result is None:
            print("Job not found.")
            return

        print(f"\nSkill profile for {result['job_title']}:")
        for skill, value in result["skills"].items():
            print(f"  {skill}: {value:.2f}")

        print(f"\nAI Exposure Index: {result['ai_exposure']:.2f}")

    else:
        print("Invalid option.")


# Check that the selected skill number exists in the dataset
def valid_skill_number(skill_number):
    return 1 <= skill_number <= 10


# Convert a number like 3 into the column name "Skill_3"
def skill_column(skill_number):
    return f"Skill_{skill_number}"


# Return all rows where the chosen skill is at least the minimum level
def filter_by_skill(data, skill_number, min_level):
    col = skill_column(skill_number)
    return data[data[col] >= min_level]


# Return a sorted list of job titles that match the selected skill filter
def jobs_by_skill(data, skill_number, min_level):
    filtered = filter_by_skill(data, skill_number, min_level)

    if filtered.empty:
        return []

    jobs = filtered["Job_Title"].dropna().unique().tolist()
    jobs.sort()  # keeps output consistent
    return jobs


# Calculate the average AI exposure for jobs matching the selected skill filter
def average_ai_exposure_by_skill(data, skill_number, min_level):
    filtered = filter_by_skill(data, skill_number, min_level)

    if filtered.empty:
        return None

    return filtered["AI_Exposure_Index"].mean()


# Show the top matching jobs based on the selected skill value
def top_jobs_by_skill(data, skill_number, min_level, top_n=10):
    filtered = filter_by_skill(data, skill_number, min_level)

    if filtered.empty:
        return pd.DataFrame()

    col = skill_column(skill_number)
    top = filtered.sort_values(by=col, ascending=False)
    return top[["Job_Title", col, "AI_Exposure_Index"]].head(top_n)


# Return the skill profile and AI exposure for the first matching job title
def skill_profile_by_job(data, job_title):
    # Case-insensitive partial match
    matches = data[
        data["Job_Title"].str.lower().str.contains(job_title.lower(), na=False)
    ]

    if matches.empty:
        return None

    row = matches.iloc[0]

    # Store all 10 skill values in a dictionary
    skills = {f"Skill_{i}": row[f"Skill_{i}"] for i in range(1, 11)}

    return {
        "job_title": row["Job_Title"],
        "skills": skills,
        "ai_exposure": row["AI_Exposure_Index"]
    }