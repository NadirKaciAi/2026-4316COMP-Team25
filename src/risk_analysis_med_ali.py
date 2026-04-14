import matplotlib.pyplot as plt
from collections import Counter

# import DataLoader from your project
from data_loader_Aymen import DataLoader


# ----------------------------
# Load Data from DataLoader
# ----------------------------

def load_data():

    loader = DataLoader()

    data = loader.load_data()

    return data


# ----------------------------
# Convert string to float safely
# ----------------------------

def get_probability(job):

    try:
        return float(job["Automation_Probability_2030"])

    except:
        return 0


# ----------------------------
# 1️⃣ Top 10 Jobs
# ----------------------------

def top_10_jobs(data):

    sorted_jobs = sorted(
        data,
        key=get_probability,
        reverse=True
    )

    top10 = sorted_jobs[:10]

    print("\nTop 10 Highest Automation Risk Jobs:\n")

    job_titles = []
    probabilities = []

    for job in top10:

        title = job["Job_Title"]
        prob = get_probability(job)

        print(title, "-", prob)

        job_titles.append(title)
        probabilities.append(prob)

    # Bar Chart
    plt.figure()

    plt.barh(job_titles, probabilities)

    plt.title("Top 10 Highest Automation Risk Jobs")

    plt.tight_layout()

    plt.savefig("top10_jobs.png")

    plt.show()


# ----------------------------
# 2️⃣ Jobs by Risk Category
# ----------------------------

def jobs_by_risk(data):

    categories = []

    for job in data:

        categories.append(
            job["Risk_Category"]
        )

    counts = Counter(categories)

    print("\nJobs by Risk Category:\n")

    for k, v in counts.items():

        print(k, ":", v)

    plt.figure()

    plt.pie(
        counts.values(),
        labels=counts.keys(),
        autopct="%1.1f%%"
    )

    plt.title("Jobs by Risk Category")

    plt.tight_layout()

    plt.savefig("risk_category.png")

    plt.show()


# ----------------------------
# 3️⃣ Average by Education
# ----------------------------

def avg_risk_by_education(data):

    education_dict = {}

    for job in data:

        edu = job["Education_Level"]

        prob = get_probability(job)

        if edu not in education_dict:

            education_dict[edu] = []

        education_dict[edu].append(prob)

    averages = {}

    for edu in education_dict:

        avg = sum(
            education_dict[edu]
        ) / len(
            education_dict[edu]
        )

        averages[edu] = avg

    print("\nAverage Risk by Education:\n")

    for edu, avg in averages.items():

        print(edu, ":", round(avg, 2))

    plt.figure()

    plt.bar(
        list(averages.keys()),
        list(averages.values())
    )

    plt.title(
        "Average Automation Risk by Education"
    )

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig("education_risk.png")

    plt.show()


# ----------------------------
# 4️⃣ Filter High Risk Jobs
# ----------------------------

def filter_high_risk(data):

    print("\nHigh Risk Jobs (>70%):\n")

    count = 0

    for job in data:

        prob = get_probability(job)

        if prob > 0.7:

            print(
                job["Job_Title"],
                "-",
                prob
            )

            count += 1

            if count == 10:

                break


# =================================================
# 🔵 MINI MENU (IMPORTANT)
# =================================================

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