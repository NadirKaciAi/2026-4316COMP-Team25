from data_loader_Aymen import DataLoader


# =========================
# Function 1: Search jobs by keyword
# =========================
def search_jobs_by_keyword(data):
    keyword = input("\nEnter a keyword to search jobs (or '1' to return): ").strip().lower()

    if keyword == '1':
        print("Returning to Jobs by Keyword menu...")
        return

    results = []

    for item in data:
        job_title = item["Job_Title"].lower()
        if keyword in job_title:
            results.append(item)

    if not results:
        print(f"No jobs found containing '{keyword}'.")
        return

    print(f"\nJobs matching '{keyword}':")
    for job in results:
        print(f"- {job['Job_Title']}")


# =========================
# Function 2: Detailed search (with extra info)
# =========================
def search_jobs_with_details(data):
    keyword = input("\nEnter a keyword (or '1' to return): ").strip().lower()

    if keyword == '1':
        print("Returning to Jobs by Keyword menu...")
        return

    results = []

    for item in data:
        if keyword in item["Job_Title"].lower():
            results.append(item)

    if not results:
        print(f"No jobs found for '{keyword}'.")
        return

    print(f"\nDetailed Results for '{keyword}':")
    print("Job | Growth | Risk")
    print("-----------------------------------")

    for job in results:
        try:
            growth = float(job["Tech_Growth_Factor"])
            risk = float(job["Automation_Probability_2030"])
        except:
            growth = "N/A"
            risk = "N/A"

        print(f"{job['Job_Title']} | {growth} | {risk}")


# =========================
# Function 3: Count matches
# =========================
def count_jobs_by_keyword(data):
    keyword = input("\nEnter a keyword (or '1' to return): ").strip().lower()

    if keyword == '1':
        print("Returning to Jobs by Keyword menu...")
        return

    count = 0

    for item in data:
        if keyword in item["Job_Title"].lower():
            count += 1

    print(f"\nNumber of jobs containing '{keyword}': {count}")


# =========================
# MAIN MENU FUNCTION
# =========================
def run_jobs_by_keyword():
    loader = DataLoader()
    data = loader.load_data()

    if not data:
        print("No data available.")
        return

    while True:
        print("\n" + "="*50)
        print("            JOBS BY KEYWORD")
        print("="*50)
        print("1. Search job titles")
        print("2. Search with details (Growth & Risk)")
        print("3. Count jobs by keyword")
        print("4. Return to main menu")
        print("="*50)

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            search_jobs_by_keyword(data)

        elif choice == "2":
            search_jobs_with_details(data)

        elif choice == "3":
            count_jobs_by_keyword(data)

        elif choice == "4":
            print("Returning to main menu...")
            break

        else:
            print("Invalid choice. Try again.")


# =========================
# RUN FILE DIRECTLY
# =========================
if __name__ == "__main__":
    run_jobs_by_keyword()