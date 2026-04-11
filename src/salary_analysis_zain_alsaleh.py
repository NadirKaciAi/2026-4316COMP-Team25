import csv

def load_data():
    data = []
    try:
        with open("data.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row["Average_Salary"] != "":
                    try:
                        row["Average_Salary"] = float(row["Average_Salary"])
                        data.append(row)
                    except:
                        pass

        print("Loaded", len(data), "rows")

    except FileNotFoundError:
        print("data.csv not found")

    return data


def overall_average_salary(data):
    if len(data) == 0:
        print("No data available")
        return

    total = 0
    for row in data:
        total = total + row["Average_Salary"]

    average = total / len(data)
    print("Overall Average Salary: £{:.2f}".format(average))


def top_10_jobs(data):
    if len(data) == 0:
        print("No data available")
        return

    sorted_data = sorted(data, key=lambda row: row["Average_Salary"], reverse=True)

    print("\nTop 10 Highest Paying Jobs:")
    count = 0
    for row in sorted_data:
        if count < 10:
            print(row["Job_Title"], "- £{:.2f}".format(row["Average_Salary"]))
            count = count + 1


def avg_salary_by_education(data):
    if len(data) == 0:
        print("No data available")
        return

    education_totals = {}
    education_counts = {}

    for row in data:
        education = row["Education_Level"]
        salary = row["Average_Salary"]

        if education in education_totals:
            education_totals[education] = education_totals[education] + salary
            education_counts[education] = education_counts[education] + 1
        else:
            education_totals[education] = salary
            education_counts[education] = 1

    print("\nAverage Salary by Education Level:")
    for education in education_totals:
        average = education_totals[education] / education_counts[education]
        print(education, "- £{:.2f}".format(average))


def menu():
    data = load_data()

    while True:
        print("\n===== Salary Insights Menu =====")
        print("1. Overall Average Salary")
        print("2. Top 10 Highest Paying Jobs")
        print("3. Average Salary by Education Level")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            overall_average_salary(data)
        elif choice == "2":
            top_10_jobs(data)
        elif choice == "3":
            avg_salary_by_education(data)
        elif choice == "4":
            print("Goodbye")
            break
        else:
            print("Invalid choice")


menu()