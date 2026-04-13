from data_loader_Aymen import DataLoader

def top_10_jobs(data):
    valid_rows = []
    for row in data:
        try:
            valid_rows.append({**row, "Average_Salary": float(row["Average_Salary"])})
        except (ValueError, KeyError):
            pass

    sorted_data = sorted(valid_rows, key=lambda r: r["Average_Salary"], reverse=True)
    print("\nTop 10 Highest Paying Jobs:")
    for row in sorted_data[:10]:
        print("  {} - £{:.2f}".format(row["Job_Title"], row["Average_Salary"]))


def avg_salary_by_education(data):
    totals, counts = {}, {}
    for row in data:
        try:
            edu = row["Education_Level"]
            salary = float(row["Average_Salary"])
        except (ValueError, KeyError):
            continue
        totals[edu] = totals.get(edu, 0) + salary
        counts[edu] = counts.get(edu, 0) + 1

    print("\nAverage Salary by Education Level:")
    for edu in totals:
        print("  {} - £{:.2f}".format(edu, totals[edu] / counts[edu]))


def salary_by_risk_category(data):
    totals, counts = {}, {}
    for row in data:
        try:
            risk = row["Risk_Category"]
            salary = float(row["Average_Salary"])
        except (ValueError, KeyError):
            continue
        totals[risk] = totals.get(risk, 0) + salary
        counts[risk] = counts.get(risk, 0) + 1

    print("\nAverage Salary by AI Automation Risk Category:")
    for risk in ["Low", "Medium", "High"]:
        if risk in totals:
            print("  {} Risk - £{:.2f} ({} jobs)".format(
                risk, totals[risk] / counts[risk], counts[risk]))


def high_salary_low_risk(data):
    valid_rows = []
    for row in data:
        try:
            valid_rows.append({
                **row,
                "Average_Salary": float(row["Average_Salary"]),
                "Automation_Probability_2030": float(row["Automation_Probability_2030"])
            })
        except (ValueError, KeyError):
            pass

    if not valid_rows:
        print("No data available.")
        return

    avg_salary = sum(r["Average_Salary"] for r in valid_rows) / len(valid_rows)

    results = [
        r for r in valid_rows
        if r["Average_Salary"] > avg_salary and r["Risk_Category"] == "Low"
    ]

    results.sort(key=lambda r: r["Average_Salary"], reverse=True)

    print("\nHigh-Paying Jobs with Low Automation Risk (above avg £{:.0f}):".format(avg_salary))
    for row in results[:10]:
        print("  {} - £{:.2f} | Automation Prob: {:.0%}".format(
            row["Job_Title"], row["Average_Salary"], row["Automation_Probability_2030"]))


def salary_vs_ai_exposure(data):
    search = input("\nEnter job title to search (or press Enter to see all): ").strip().lower()

    job_data = {}
    for row in data:
        try:
            title = row["Job_Title"]
            salary = float(row["Average_Salary"])
            exposure = float(row["AI_Exposure_Index"])
        except (ValueError, KeyError):
            continue

        if search == "" or search in title.lower():
            if title not in job_data:
                job_data[title] = {"salaries": [], "exposures": []}
            job_data[title]["salaries"].append(salary)
            job_data[title]["exposures"].append(exposure)

    if not job_data:
        print("No jobs found matching '{}'.".format(search))
        return

    print("\nSalary vs AI Exposure for '{}':".format(search if search else "all jobs"))
    print("-" * 60)

    for title, values in sorted(job_data.items()):
        avg_salary = sum(values["salaries"]) / len(values["salaries"])
        avg_exposure = sum(values["exposures"]) / len(values["exposures"])
        sample_size = len(values["salaries"])

        if avg_exposure <= 0.33:
            level = "Low"
        elif avg_exposure <= 0.66:
            level = "Medium"
        else:
            level = "High"

        print("  {} - Avg Salary: £{:.2f} | Avg AI Exposure: {:.2f} ({}) | Sample: {}".format(
            title, avg_salary, avg_exposure, level, sample_size))


def run_salary_analysis():
    loader = DataLoader()
    data = loader.load_data()

    while True:
        print("\n===== Salary Analysis =====")
        print("1. Top 10 Highest Paying Jobs")
        print("2. Average Salary by Education Level")
        print("3. Average Salary by AI Risk Category")
        print("4. High-Paying Jobs with Low Automation Risk")
        print("5. Salary vs AI Exposure (Search by Job Title)")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            top_10_jobs(data)
        elif choice == "2":
            avg_salary_by_education(data)
        elif choice == "3":
            salary_by_risk_category(data)
        elif choice == "4":
            high_salary_low_risk(data)
        elif choice == "5":
            salary_vs_ai_exposure(data)
        elif choice == "6":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    run_salary_analysis()