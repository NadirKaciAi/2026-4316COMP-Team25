# ---------------------------------------------------------
# risk_analysis_med_ali.py
# 
# Task 1 (Group): Implementation of Automation Risk Analysis
# Task 2 (Individual): Text-based Data Visualisation
# ---------------------------------------------------------
import csv
import os

def run_risk_analysis():
    file_path = os.path.join('data', 'data.csv')
    
    data = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
        print(f"Successfully loaded {len(data)} rows from data.csv")
    except FileNotFoundError:
        print(f"Error: Still cannot find data.csv at {file_path}")
        return

    while True:
        print("\n" + "*"*26)
        print(" AUTOMATION RISK ANALYSIS  ")
        print("*"*26)
        print("1. View Top 10 High-Risk Jobs")
        print("2. Summary & Text-Chart (By Education)")
        print("3. Exit to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            sorted_jobs = sorted(data, key=lambda x: float(x.get('Automation_Probability_2030', 0)), reverse=True)
            print("\nTop 10 High-Risk Jobs (2030):")
            for i, job in enumerate(sorted_jobs[:10], 1):
                print(f"{i}. {job['Job_Title']} - {float(job['Automation_Probability_2030']):.1%}")

        elif choice == "2":
          
            stats = {}
            for row in data:
                edu = row.get('Education_Level', 'Other')
                prob = float(row.get('Automation_Probability_2030', 0))
                if edu not in stats: stats[edu] = [0, 0]
                stats[edu][0] += prob
                stats[edu][1] += 1

            print("\nRISK SUMMARY & VISUALISATION:")
            for edu, val in stats.items():
                avg = val[0] / val[1]
            
                bar = "" * int(avg * 20)
                print(f"{edu:<20} | {avg:.2f} {bar}")

        elif choice == "3":
            break

if __name__ == "__main__":
    run_risk_analysis()