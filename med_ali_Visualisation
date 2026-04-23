# ---------------------------------------------------------
# risk_analysis_med_ali.py 
# Professional Hybrid Version: 2 Graphs + Strong Logic
# ---------------------------------------------------------

import csv
import os
from collections import Counter
from data_loader_Aymen import DataLoader

# Check for Matplotlib to avoid 'ModuleNotFoundError' on your Mac
try:
    import matplotlib.pyplot as plt
    HAS_PLOT = True
except ImportError:
    HAS_PLOT = False

def load_data():
    """Fetches data using the team's DataLoader."""
    loader = DataLoader()
    return loader.load_data()

def get_probability(job):
    """Converts string probability to float for math operations."""
    try:
        return float(job["Automation_Probability_2030"])
    except (KeyError, ValueError):
        return 0

# ==========================================
# 1. Top 10 Jobs (Text Only - No Graph)
# ==========================================
def top_10_jobs(data):
    sorted_jobs = sorted(data, key=get_probability, reverse=True)
    print("\nTop 10 Highest Automation Risk Jobs:\n")
    for i, job in enumerate(sorted_jobs[:10], start=1):
        # Using :.1% makes 0.85 look like 85.0% for your report
        print(f"{i}. {job['Job_Title']:<30} - {get_probability(job):.1%}")

# ==========================================
# 2. Risk Categories (GRAPH 1: Pie Chart)
# ==========================================
def jobs_by_risk(data):
    categories = [job["Risk_Category"] for job in data if "Risk_Category" in job]
    counts = Counter(categories)

    print("\nJobs by Risk Category Summary:")
    for category, count in counts.items():
        print(f" - {category}: {count}")

    if HAS_PLOT:
        # Visualisation for Task 2
        plt.figure(figsize=(7, 7))
        plt.pie(counts.values(), labels=counts.keys(), autopct='%1.1f%%', startangle=140)
        plt.title('Job Distribution by Risk Category', fontweight='bold')
        plt.show()
    else:
        print("\n[Note] Install Matplotlib to see the Pie Chart: python3 -m pip install matplotlib")

# ==========================================
# 3. Education Avg (GRAPH 2: Bar Chart)
# ==========================================
def avg_risk_by_education(data):
    education_dict = {}
    for job in data:
        edu = job.get("Education_Level", "Other")
        prob = get_probability(job)
        if edu not in education_dict:
            education_dict[edu] = []
        education_dict[edu].append(prob)

    labels, averages = [], []
    print("\nAverage Risk by Education Level:")
    for edu, probs in education_dict.items():
        avg = sum(probs) / len(probs)
        labels.append(edu)
        averages.append(avg)
        print(f" - {edu}: {avg:.2f}")

    if HAS_PLOT:
        # Bar Chart similar to Zain's style
        plt.figure(figsize=(10, 6))
        plt.bar(labels, averages, color='skyblue', edgecolor='navy')
        plt.title('Avg Automation Risk vs Education', fontweight='bold')
        plt.ylabel('Risk Probability')
        plt.xticks(rotation=30)
        plt.tight_layout()
        plt.show()

# ==========================================
# 4. Filter High Risk (Text Only - No Graph)
# ==========================================
def filter_high_risk(data):
    print("\nHigh Risk Jobs Filter (>70%):\n")
    high_risk = [job for job in data if get_probability(job) > 0.7]
    high_risk = sorted(high_risk, key=get_probability, reverse=True)

    for i, job in enumerate(high_risk[:10], start=1):
        print(f"{i}. {job['Job_Title']:<30} - {get_probability(job):.1%}")

# =========================
# MAIN MENU
# =========================
def run_risk_analysis():
    data = load_data()
    if not data:
        print("Dataset load failed.")
        return

    while True:
        print("\n" + "="*45)
        print("    AUTOMATION RISK ANALYSIS MODULE")
        print("="*45)
        print("1. Top 10 Highest Risk Jobs (Text)")
        print("2. Risk Category Distribution (Pie Chart)")
        print("3. Average Risk by Education (Bar Chart)")
        print("4. List High Risk Jobs > 70% (Text)")
        print("5. Exit to Team Menu")
        print("="*45)

        choice = input("Select an option (1-5): ").strip()

        if choice == "1": top_10_jobs(data)
        elif choice == "2": jobs_by_risk(data)
        elif choice == "3": avg_risk_by_education(data)
        elif choice == "4": filter_high_risk(data)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run_risk_analysis()