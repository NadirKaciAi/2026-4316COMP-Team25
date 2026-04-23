# ---------------------------------------------------------
# risk_analysis_med_ali.py 
# Professional Hybrid Version: Logic + Visualisations
# ---------------------------------------------------------

import csv
import os
from collections import Counter
from data_loader_Aymen import DataLoader

# Try to import matplotlib for Task 2 visualisation
try:
    import matplotlib.pyplot as plt
    HAS_PLOT = True
except ImportError:
    HAS_PLOT = False

def load_data():
    """Uses the group DataLoader to fetch the CSV data."""
    loader = DataLoader()
    return loader.load_data()

def get_probability(job):
    """Safely converts string probability to a float."""
    try:
        return float(job["Automation_Probability_2030"])
    except (KeyError, ValueError):
        return 0

# =========================
# Feature 1: Top 10 Jobs
# =========================
def top_10_jobs(data):
    sorted_jobs = sorted(data, key=get_probability, reverse=True)
    top10 = sorted_jobs[:10]

    print("\nTop 10 Highest Automation Risk Jobs:\n")
    for i, job in enumerate(top10, start=1):
        print(f"{i}. {job['Job_Title']} - {get_probability(job):.2%}")

# =========================
# Feature 2: Risk Category (Graph included)
# =========================
def jobs_by_risk(data):
    categories = [job["Risk_Category"] for job in data if "Risk_Category" in job]
    counts = Counter(categories)

    print("\nJobs by Risk Category:\n")
    for category, count in counts.items():
        print(f"{category}: {count}")

    if HAS_PLOT:
        # Pie Chart Visualisation
        plt.figure(figsize=(8, 8))
        plt.pie(counts.values(), labels=counts.keys(), autopct='%1.1f%%', startangle=140)
        plt.title('Distribution of Jobs by Risk Category', fontweight='bold')
        plt.show()

# =========================
# Feature 3: Education Avg (Graph included)
# =========================
def avg_risk_by_education(data):
    education_dict = {}
    for job in data:
        edu = job.get("Education_Level", "Other")
        prob = get_probability(job)
        if edu not in education_dict:
            education_dict[edu] = []
        education_dict[edu].append(prob)

    labels = []
    averages = []
    print("\nAverage Risk by Education:\n")
    for edu, probs in education_dict.items():
        avg = sum(probs) / len(probs)
        labels.append(edu)
        averages.append(avg)
        print(f"{edu}: {avg:.2f}")

    if HAS_PLOT:
        # Bar Chart Visualisation similar to Team Example
        plt.figure(figsize=(10, 6))
        plt.bar(labels, averages, color='skyblue', edgecolor='navy')
        plt.title('Avg Automation Risk by Education Level', fontweight='bold')
        plt.ylabel('Risk Probability')
        plt.xticks(rotation=30)
        plt.tight_layout()
        plt.show()

# =========================
# Feature 4: Filter High Risk
# =========================
def filter_high_risk(data):
    print("\nHigh Risk Jobs (>70%):\n")
    high_risk = [job for job in data if get_probability(job) > 0.7]
    high_risk = sorted(high_risk, key=get_probability, reverse=True)

    for i, job in enumerate(high_risk[:10], start=1):
        print(f"{i}. {job['Job_Title']} - {get_probability(job):.2%}")

# =========================
# MAIN MENU
# =========================
def run_risk_analysis():
    data = load_data()
    if not data:
        print("Error: Could not load data.")
        return

    while True:
        print("\n=== Automation Risk Analysis (LJMU Version) ===")
        print("1. Top 10 Highest Risk Jobs")
        print("2. Jobs by Risk Category (View Graph)")
        print("3. Average Risk by Education (View Graph)")
        print("4. Filter High Risk Jobs (>70%)")
        print("5. Return to Main Menu")

        choice = input("Enter choice (1-5): ").strip()

        if choice == "1": top_10_jobs(data)
        elif choice == "2": jobs_by_risk(data)
        elif choice == "3": avg_risk_by_education(data)
        elif choice == "4": filter_high_risk(data)
        elif choice == "5":
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    run_risk_analysis()
    