# ---------------------------------------------------------
# skill_analysis_Parsa_Siri.py
#
# This file handles all skill-related analysis for the project.
# The user can either:
# 1. Find jobs by skill level and view its AI exposure
# 2. View the full skill profile of a chosen job and its AI exposure
# ---------------------------------------------------------

#Import Data Loader
from data_loader import DataLoader
loader = DataLoader()
data_raw = loader.load_data()


# Convert Skill_1-10 and AI_Exposure_Index from strings to floats
def convert_numeric_fields(data):
    numeric_cols = [f"Skill_{i}" for i in range(1, 11)] + ["AI_Exposure_Index"]
    converted = []
    for row in data:
        row = dict(row)
        for col in numeric_cols:
            if col in row:
                try:
                    row[col] = float(row[col])
                except (ValueError, TypeError):
                    row[col] = None
        row["Job_Title"] = str(row.get("Job_Title", "")).strip()
        converted.append(row)
    return converted


# Check that the selected skill number exists in the dataset
def valid_skill_number(skill_number):
    return 1 <= skill_number <= 10


# Convert a number like 3 into the column name "Skill_3"
def skill_column(skill_number):
    return f"Skill_{skill_number}"


# Return all rows where the chosen skill is at least the minimum level
def filter_by_skill(data, skill_number, min_level):
    col = skill_column(skill_number)
    return [row for row in data if row.get(col) is not None and row[col] >= min_level]


# Return a sorted list of job titles that match the selected skill filter
def jobs_by_skill(data, skill_number, min_level):
    filtered = filter_by_skill(data, skill_number, min_level)
    jobs = list({row["Job_Title"] for row in filtered if row.get("Job_Title")})
    jobs.sort()
    return jobs


# Calculate the average AI exposure for jobs matching the selected skill filter
def average_ai_exposure_by_skill(data, skill_number, min_level):
    filtered = filter_by_skill(data, skill_number, min_level)
    exposures = [row["AI_Exposure_Index"] for row in filtered if row.get("AI_Exposure_Index") is not None]

    if not exposures:
        return None

    return sum(exposures) / len(exposures)


# Show the top matching jobs based on the selected skill value
def top_jobs_by_skill(data, skill_number, min_level, top_n=10):
    filtered = filter_by_skill(data, skill_number, min_level)
    col = skill_column(skill_number)
    sorted_jobs = sorted(filtered, key=lambda row: row.get(col, 0), reverse=True)
    return sorted_jobs[:top_n]


# Return the skill profile and AI exposure for the first matching job title
def skill_profile_by_job(data, job_title):
    matches = [
        row for row in data
        if job_title.lower() in row.get("Job_Title", "").lower()
    ]

    if not matches:
        return None

    row = matches[0]
    skills = {f"Skill_{i}": row[f"Skill_{i}"] for i in range(1, 11)}

    return {
        "job_title": row["Job_Title"],
        "skills": skills,
        "ai_exposure": row["AI_Exposure_Index"]
    }


# Main function to run the skill analysis menu and handle user choices
def run_skill_analysis():
    # Convert numeric fields so comparisons and calculations work correctly
    data_local = convert_numeric_fields(data_raw)

    print("\nSkill Analysis")
    print("1. Find jobs by skill level and view AI exposure")
    print("2. View a job's skill profile and AI exposure")

    choice = input("Choose an option: ").strip()

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

        jobs = jobs_by_skill(data_local, skill_number, min_level)
        avg_exposure = average_ai_exposure_by_skill(data_local, skill_number, min_level)
        top_jobs = top_jobs_by_skill(data_local, skill_number, min_level)

        if not jobs:
            print("No matching jobs found.")
            return

        print(f"\nJobs with Skill_{skill_number} >= {min_level}:")
        for job in jobs:
            print("-", job)

        print(f"\nTotal jobs found: {len(jobs)}")
        if avg_exposure is not None:
            print(f"Average AI Exposure Index: {avg_exposure:.2f}")
        else:
            print("Average AI Exposure Index: N/A")

        print("\nTop matches:")
        for row in top_jobs:
            print(f"  {row['Job_Title']:<40} Skill_{skill_number}: {row[skill_column(skill_number)]:.2f}  AI_Exposure_Index: {row['AI_Exposure_Index']:.2f}")

    elif choice == "2":
        job_title = input("Enter a job title: ").strip()
        result = skill_profile_by_job(data_local, job_title)

        if result is None:
            print("Job not found.")
            return

        print(f"\nSkill profile for {result['job_title']}:")
        for skill, value in result["skills"].items():
            print(f"  {skill}: {value:.2f}")

        print(f"\nAI Exposure Index: {result['ai_exposure']:.2f}")

    else:
        print("Invalid option.")


if __name__ == "__main__":
    run_skill_analysis()