import csv

# Load data
def load_data():
    data = []
    try:
        with open("data.csv", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                salary = row["Average_Salary"].strip()

                if salary != "":
                    try:
                        row["Average_Salary"] = float(salary)
                        data.append(row)
                    except ValueError:
                        continue  # skip invalid values

        print(f"✅ Loaded {len(data)} valid rows")

    except FileNotFoundError:
        print("❌ File not found. Make sure 'data.csv' is in the same folder.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

    return data

data = load_data()

def overall_average_salary():
    if not data:
        print("⚠️ No data available.")
        return

    total = sum(row["Average_Salary"] for row in data)
    avg = total / len(data)
    print(f"\n💰 Overall Average Salary: £{avg:,.2f}")

def top_10_jobs():
    if not data:
        print("⚠️ No data available.")
        return

    sorted_data = sorted(data, key=lambda x: x["Average_Salary"], reverse=True)
    top10 = sorted_data[:10]

    print("\n🔥 Top 10 Highest Paying Jobs:\n")
    for job in top10:
        print(f"{job['Job_Title']} - £{job['Average_Salary']:,.2f}")

def avg_salary_by_education():
    if not data:
        print("⚠️ No data available.")
        return

    grouped = {}

    for row in data:
        edu = row["Education_Level"]
        salary = row["Average_Salary"]

        if edu not in grouped:
            grouped[edu] = []
        grouped[edu].append(salary)

    print("\n🎓 Average Salary by Education Level:\n")
    for edu, salaries in grouped.items():
        avg = sum(salaries) / len(salaries)
        print(f"{edu}: £{avg:,.2f}")

def menu():
    while True:
        print("\n===== Salary Insights Menu =====")
        print("1. Overall Average Salary")
        print("2. Top 10 Highest Paying Jobs")
        print("3. Average Salary by Education Level")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            overall_average_salary()
        elif choice == "2":
            top_10_jobs()
        elif choice == "3":
            avg_salary_by_education()
        elif choice == "4":
            print("Exiting... 👋")
            break
        else:
            print("❌ Invalid choice, try again.")

# Run program
menu()