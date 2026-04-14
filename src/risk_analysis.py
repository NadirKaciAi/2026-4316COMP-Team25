import pandas as pd
import matplotlib.pyplot as plt


# ----------------------------
# Load Dataset
# ----------------------------

def load_data():

    df = pd.read_csv("AI_Impact_on_Jobs_2030.csv")

    return df


# ----------------------------
# Top 10 Jobs
# ----------------------------

def top_10_jobs(df):

    top10 = df.sort_values(
        by="Automation_Probability_2030",
        ascending=False
    ).head(10)

    print("\nTop 10 Highest Automation Risk Jobs:\n")

    print(top10[
        ["Job_Title",
         "Automation_Probability_2030"]
    ])

    plt.figure()

    plt.barh(
        top10["Job_Title"],
        top10["Automation_Probability_2030"]
    )

    plt.title("Top 10 Highest Automation Risk Jobs")

    plt.tight_layout()

    plt.savefig("top10_jobs.png")

    plt.show()


# ----------------------------
# Jobs by Risk Category
# ----------------------------

def jobs_by_risk(df):

    risk_counts = df["Risk_Category"].value_counts()

    print("\nJobs by Risk Category:\n")

    print(risk_counts)

    plt.figure()

    plt.pie(
        risk_counts,
        labels=risk_counts.index,
        autopct="%1.1f%%"
    )

    plt.title("Jobs by Risk Category")

    plt.tight_layout()

    plt.savefig("risk_category.png")

    plt.show()


# ----------------------------
# Average by Education
# ----------------------------

def avg_risk_by_education(df):

    avg_by_edu = df.groupby(
        "Education_Level"
    )["Automation_Probability_2030"].mean()

    print("\nAverage Automation Risk by Education:\n")

    print(avg_by_edu)

    plt.figure()

    plt.bar(
        avg_by_edu.index,
        avg_by_edu.values
    )

    plt.title(
        "Average Automation Risk by Education"
    )

    plt.tight_layout()

    plt.savefig("education_risk.png")

    plt.show()


# ----------------------------
# Filter High Risk
# ----------------------------

def filter_high_risk(df):

    high_risk_jobs = df[
        df["Automation_Probability_2030"] > 0.7
    ]

    print("\nHigh Risk Jobs (>70%):\n")

    print(high_risk_jobs[
        ["Job_Title",
         "Automation_Probability_2030"]
    ].head(10))


# =================================================
# 🔵 Mini Menu for Feature 2
# =================================================

def run_risk_analysis():

    df = load_data()

    while True:

        print("\n=== Automation Risk Analysis Menu ===")

        print("1. Top 10 Highest Risk Jobs")
        print("2. Jobs by Risk Category")
        print("3. Average Risk by Education Level")
        print("4. Filter High Risk Jobs (>70%)")
        print("5. Exit to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":

            top_10_jobs(df)

        elif choice == "2":

            jobs_by_risk(df)

        elif choice == "3":

            avg_risk_by_education(df)

        elif choice == "4":

            filter_high_risk(df)

        elif choice == "5":

            print("Returning to Main Menu...")
            break

        else:

            print("Invalid choice. Try again.")