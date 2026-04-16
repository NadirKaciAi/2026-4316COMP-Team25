#emojis to be removed or agreed upon (UI in general)


#Import Data Loader
from data_loader_Aymen import DataLoader  

# Functionality 1, analyse job based on title
def single_job_analysis(data_list):
    """Analyze one job entered by the user, with input validation."""
    available_jobs = [item["Job_Title"].title() for item in data_list]

    while True:
        job_input = input("\nEnter the job title (or type '1' to return): ").strip().title()

        if job_input == '1':
            print("Returning to Growth vs Risk menu...")
            break

        if job_input not in available_jobs:
            print(f"Job '{job_input}' not found. Please type another job or press 1 to return.")
            continue

        # Job is valid
        job_data = next(item for item in data_list if item["Job_Title"].title() == job_input)
        growth = float(job_data["Tech_Growth_Factor"])
        risk = float(job_data["Automation_Probability_2030"])

        print(f"\nJob: {job_data['Job_Title']}")
        print(f"Growth potential (Tech Growth Factor): {growth}")
        print(f"Risk of automation (Probability 2030): {risk}")

        if growth > risk:
            print("Overall outlook: Positive ✅")
        elif growth < risk:
            print("Overall outlook: Risky ⚠️")
        else:
            print("Overall outlook: Neutral ⚖️")

        break  # exit after analysis

#Funcionality 2,compare jobs stats by job title
def compare_multiple_jobs(data_list):
    """Compare 2-3 jobs entered by the user."""
    available_jobs = [item["Job_Title"].title() for item in data_list]

    while True:
        jobs_input = input("\nEnter 2-3 job titles separated by commas (or '1' to return): ").strip()
        if jobs_input == '1':
            print("Returning to Growth vs Risk menu...")
            break

        jobs = [job.strip().title() for job in jobs_input.split(",")][:3]
        print("\nComparison Table:\nJob | Growth | Risk | Outlook")
        print("-----------------------------------------")
        for job in jobs:
            if job not in available_jobs:
                print(f"{job} | N/A | N/A | Job not found")
                continue
            job_data = next(item for item in data_list if item["Job_Title"].title() == job)
            growth = float(job_data["Tech_Growth_Factor"])
            risk = float(job_data["Automation_Probability_2030"])
            outlook = "Positive ✅" if growth > risk else "Risky ⚠️" if growth < risk else "Neutral ⚖️"
            print(f"{job_data['Job_Title']} | {growth} | {risk} | {outlook}")
        break  # exit after comparison

# Funcionality 2, jobs by ratio 
def top_jobs_by_ratio(data_list):
    """Show top 5 jobs by growth-to-risk ratio."""
    jobs_with_ratio = []
    for item in data_list:
        growth = float(item["Tech_Growth_Factor"])
        risk = float(item["Automation_Probability_2030"])
        ratio = growth / risk if risk != 0 else float('inf')
        jobs_with_ratio.append((item["Job_Title"], growth, risk, ratio))

    jobs_sorted = sorted(jobs_with_ratio, key=lambda x: x[3], reverse=True)

    print("\nTop 5 Jobs by Growth-to-Risk Ratio:")
    print("Job | Growth | Risk | Growth/Risk Ratio")
    print("-----------------------------------------")
    for job, growth, risk, ratio in jobs_sorted[:5]:
        print(f"{job} | {growth} | {risk} | {ratio:.2f}")

#Funcionality number 3, 
def visual_analysis(data_list):
    """Simple text-based visual analysis for top 5 jobs."""
    jobs_sorted = sorted(data_list, key=lambda x: float(x["Tech_Growth_Factor"]) - float(x["Automation_Probability_2030"]), reverse=True)[:5]
    print("\nText-Based Visual Analysis (Growth vs Risk):")
    for item in jobs_sorted:
        growth = float(item["Tech_Growth_Factor"])
        risk = float(item["Automation_Probability_2030"])
        bar_growth = "#" * int(growth)
        bar_risk = "-" * int(risk)
        print(f"{item['Job_Title'][:15]:15} | Growth: {bar_growth} ({growth}) | Risk: {bar_risk} ({risk})")

#Main feature menu
def run_growth_vs_risk_analysis():
    """Mini-menu for the Growth vs Risk Analysis feature."""
    loader = DataLoader()
    data_list = loader.load_data()
    if not data_list:
        print("No data available. Please check your CSV file.")
        return

    while True:
        print("\n*** Growth vs Risk Analysis ***")
        print("1. Analyze a single job")
        print("2. Compare multiple jobs")
        print("3. Show top jobs by growth-to-risk ratio")
        print("4. Visual analysis of top jobs")
        print("5. Return to main menu")

        choice = input("Choose an option: ").strip()
        if choice == '1':
            single_job_analysis(data_list)
        elif choice == '2':
            compare_multiple_jobs(data_list)
        elif choice == '3':
            top_jobs_by_ratio(data_list)
        elif choice == '4':
            visual_analysis(data_list)
        elif choice == '5':
            break
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    run_growth_vs_risk_analysis()