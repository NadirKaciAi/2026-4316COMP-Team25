from data_loader_Aymen import DataLoader  # import custom data loader

def top_10_jobs(data):
    valid_rows = []  # store rows with valid salary values
    for row in data:
        try:
            # convert salary to float and keep row
            valid_rows.append({**row, "Average_Salary": float(row["Average_Salary"])})
        except (ValueError, KeyError):
            pass  # skip invalid or missing data

    # sort jobs by salary (highest first)
    sorted_data = sorted(valid_rows, key=lambda r: r["Average_Salary"], reverse=True)

    print("\nTop 10 Highest Paying Jobs:")
    for row in sorted_data[:10]:  # print top 10
        print("  {} - £{:.2f}".format(row["Job_Title"], row["Average_Salary"]))


def avg_salary_by_education(data):
    totals, counts = {}, {}  # track total salary and count per education level
    for row in data:
        try:
            edu = row["Education_Level"]
            salary = float(row["Average_Salary"])
        except (ValueError, KeyError):
            continue  # skip bad rows

        # update totals and counts
        totals[edu] = totals.get(edu, 0) + salary
        counts[edu] = counts.get(edu, 0) + 1

    print("\nAverage Salary by Education Level:")
    for edu in totals:
        # calculate and print average salary
        print("  {} - £{:.2f}".format(edu, totals[edu] / counts[edu]))


def salary_by_risk_category(data):
    totals, counts = {}, {}  # store salary totals and counts per risk level
    for row in data:
        try:
            risk = row["Risk_Category"]
            salary = float(row["Average_Salary"])
        except (ValueError, KeyError):
            continue

        totals[risk] = totals.get(risk, 0) + salary
        counts[risk] = counts.get(risk, 0) + 1

    print("\nAverage Salary by AI Automation Risk Category:")
    for risk in ["Low", "Medium", "High"]:  # keep order clean
        if risk in totals:
            print("  {} Risk - £{:.2f} ({} jobs)".format(
                risk, totals[risk] / counts[risk], counts[risk]))


def high_salary_low_risk(data):
    valid_rows = []  # store cleaned rows
    for row in data:
        try:
            # convert needed fields to float
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

    # calculate overall average salary
    avg_salary = sum(r["Average_Salary"] for r in valid_rows) / len(valid_rows)

    # filter jobs above avg salary and low risk
    results = [
        r for r in valid_rows
        if r["Average_Salary"] > avg_salary and r["Risk_Category"] == "Low"
    ]

    # sort results by salary
    results.sort(key=lambda r: r["Average_Salary"], reverse=True)

    print("\nHigh-Paying Jobs with Low Automation Risk (above avg £{:.0f}):".format(avg_salary))
    for row in results[:10]:  # shows top 10
        print("  {} - £{:.2f} | Automation Prob: {:.0%}".format(
            row["Job_Title"], row["Average_Salary"], row["Automation_Probability_2030"]))


def salary_vs_ai_exposure(data):
    # get user input (search filter)
    search = input("\nEnter job title to search (or press Enter to see all): ").strip().lower()

    job_data = {}  # store grouped salary and exposure per job
    for row in data:
        try:
            title = row["Job_Title"]
            salary = float(row["Average_Salary"])
            exposure = float(row["AI_Exposure_Index"])
        except (ValueError, KeyError):
            continue

        # filter by search keyword
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
        # compute averages
        avg_salary = sum(values["salaries"]) / len(values["salaries"])
        avg_exposure = sum(values["exposures"]) / len(values["exposures"])
        sample_size = len(values["salaries"])

        # classify exposure level
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
    data = loader.load_data()  # load dataset

    while True:
        # menu display
        print("\n===== Salary Analysis =====")
        print("1. Top 10 Highest Paying Jobs")
        print("2. Average Salary by Education Level")
        print("3. Average Salary by AI Risk Category")
        print("4. High-Paying Jobs with Low Automation Risk")
        print("5. Salary vs AI Exposure (Search by Job Title)")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        # call functions based on user choice
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
            break  # exit loop
        else:
            print("Invalid choice")


if __name__ == "__main__":
    run_salary_analysis()  # starts program