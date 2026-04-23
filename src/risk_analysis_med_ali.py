from collections import Counter

# import DataLoader from your project
from data_loader_Aymen import DataLoader

# Load Data from DataLoader

def load_data():
    loader = DataLoader()
    return loader.load_data()


# Convert string to float safely

def get_probability(job):
    try:
        return float(job["Automation_Probability_2030"])
    except:
        return 0


#  Top 10 Jobs

def top_10_jobs(data):

    sorted_jobs = sorted(
        data,
        key=get_probability,
        reverse=True
    )

    top10 = sorted_jobs[:10]

    print("\nTop 10 Highest Automation Risk Jobs:\n")

    for i, job in enumerate(top10, start=1):
        print(f"{i}. {job['Job_Title']} - {round(get_probability(job), 2)}")


# Jobs by Risk Category

def jobs_by_risk(data):

    categories = []

    for job in data:
        categories.append(job["Risk_Category"])

    counts = Counter(categories)

    print("\nJobs by Risk Category:\n")

    for category, count in counts.items():
        print(f"{category}: {count}")


#  Average by Education
def avg_risk_by_education(data):

    education_dict = {}

    for job in data:
        edu = job["Education_Level"]
        prob = get_probability(job)

        if edu not in education_dict:
            education_dict[edu] = []

        education_dict[edu].append(prob)

    print("\nAverage Risk by Education:\n")

    for edu, probs in education_dict.items():
        avg = sum(probs) / len(probs)
        print(f"{edu}: {round(avg, 2)}")


#  Filter High Risk Jobs

def filter_high_risk(data):

    print("\nHigh Risk Jobs (>70%):\n")

    high_risk = [
        job for job in data
        if get_probability(job) > 0.7
    ]

    # sort them as well (nice improvement)
    high_risk = sorted(
        high_risk,
        key=get_probability,
        reverse=True
    )

    for i, job in enumerate(high_risk[:10], start=1):
        print(f"{i}. {job['Job_Title']} - {round(get_probability(job), 2)}")



#  MINI MENU (TEXT ONLY UI)

def run_risk_analysis():

    data = load_data()

    while True:

        print("\n=== Automation Risk Analysis ===")
        print("1. Top 10 Highest Risk Jobs")
        print("2. Jobs by Risk Category")
        print("3. Average Risk by Education")
        print("4. Filter High Risk Jobs (>70%)")
        print("5. Return to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            top_10_jobs(data)

        elif choice == "2":
            jobs_by_risk(data)

        elif choice == "3":
            avg_risk_by_education(data)

        elif choice == "4":
            filter_high_risk(data)

        elif choice == "5":
            print("Returning to Main Menu...")
            break

        else:
            print("Invalid choice. Try again.")

        
        
        
if __name__ == "__main__":
 run_risk_analysis()