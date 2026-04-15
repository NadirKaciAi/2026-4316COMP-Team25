# file: ZAIN_Visualisations.py

import matplotlib.pyplot as plt

from src.data_loader_Aymen import DataLoader


def parse_valid_rows(data):
    valid = []
    for row in data:
        try:
            valid.append(
                {
                    **row,
                    "Average_Salary": float(row["Average_Salary"]),
                    "AI_Exposure_Index": float(row.get("AI_Exposure_Index", 0)),
                    "Automation_Probability_2030": float(
                        row.get("Automation_Probability_2030", 0)
                    ),
                }
            )
        except (ValueError, KeyError):
            continue
    return valid


def plot_top_10_jobs(data):
    rows = parse_valid_rows(data)
    rows.sort(key=lambda x: x["Average_Salary"], reverse=True)

    top = rows[:10]
    if not top:
        print("No valid data available for top 10 jobs.")
        return

    titles = [r.get("Job_Title", "Unknown") for r in top]
    salaries = [r["Average_Salary"] for r in top]

    plt.figure(figsize=(10, 6))
    plt.barh(titles, salaries)
    plt.xlabel("Salary (£)")
    plt.title("Top 10 Highest Paying Jobs")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()


def plot_salary_by_education(data):
    rows = parse_valid_rows(data)

    totals = {}
    counts = {}

    for row in rows:
        edu = row.get("Education_Level", "Unknown")
        totals[edu] = totals.get(edu, 0) + row["Average_Salary"]
        counts[edu] = counts.get(edu, 0) + 1

    if not totals:
        print("No valid data available for salary by education.")
        return

    labels = list(totals.keys())
    values = [totals[label] / counts[label] for label in labels]

    plt.figure(figsize=(10, 6))
    plt.bar(labels, values)
    plt.title("Average Salary by Education Level")
    plt.ylabel("Salary (£)")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()


def plot_salary_by_risk(data):
    rows = parse_valid_rows(data)

    totals = {}
    counts = {}

    for row in rows:
        risk = row.get("Risk_Category", "Unknown")
        totals[risk] = totals.get(risk, 0) + row["Average_Salary"]
        counts[risk] = counts.get(risk, 0) + 1

    if not totals:
        print("No valid data available for salary by risk category.")
        return

    labels = list(totals.keys())
    values = [totals[label] / counts[label] for label in labels]

    plt.figure(figsize=(8, 5))
    plt.bar(labels, values)
    plt.title("Salary by AI Risk Category")
    plt.ylabel("Salary (£)")
    plt.tight_layout()
    plt.show()


def plot_salary_vs_exposure(data):
    rows = parse_valid_rows(data)

    if not rows:
        print("No valid data available for salary vs AI exposure.")
        return

    salaries = [row["Average_Salary"] for row in rows]
    exposure = [row["AI_Exposure_Index"] for row in rows]

    plt.figure(figsize=(8, 5))
    plt.scatter(exposure, salaries)
    plt.xlabel("AI Exposure Index")
    plt.ylabel("Salary (£)")
    plt.title("Salary vs AI Exposure")
    plt.tight_layout()
    plt.show()


def plot_high_salary_low_risk(data):
    rows = parse_valid_rows(data)

    if not rows:
        print("No valid data available for high salary low risk analysis.")
        return

    avg_salary = sum(row["Average_Salary"] for row in rows) / len(rows)

    filtered = [
        row
        for row in rows
        if row["Average_Salary"] > avg_salary and row.get("Risk_Category") == "Low"
    ]

    filtered.sort(key=lambda x: x["Average_Salary"], reverse=True)

    if not filtered:
        print("No high salary low risk jobs found.")
        return

    titles = [row.get("Job_Title", "Unknown") for row in filtered[:10]]
    salaries = [row["Average_Salary"] for row in filtered[:10]]

    plt.figure(figsize=(10, 6))
    plt.barh(titles, salaries)
    plt.title("High Salary + Low Risk Jobs")
    plt.xlabel("Salary (£)")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()


def main():
    loader = DataLoader()
    data = loader.load_data()

    while True:
        print("\nChoose a visualisation:")
        print("1. Top 10 Highest Paying Jobs")
        print("2. Average Salary by Education Level")
        print("3. Salary by AI Risk Category")
        print("4. Salary vs AI Exposure")
        print("5. High Salary + Low Risk Jobs")
        print("0. Exit")

        choice = input("Enter your choice (0-5): ").strip()

        if choice == "1":
            plot_top_10_jobs(data)
        elif choice == "2":
            plot_salary_by_education(data)
        elif choice == "3":
            plot_salary_by_risk(data)
        elif choice == "4":
            plot_salary_vs_exposure(data)
        elif choice == "5":
            plot_high_salary_low_risk(data)
        elif choice == "0":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()