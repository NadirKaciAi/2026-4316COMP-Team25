# main_Nadir_Kaci.py
#Main menu for project, user will see this on startup, then user will have the option to choose from 7 options plus exit

# Import functionality fro respective features
from growth_analysis_Nadir_Kaci import run_growth_vs_risk_analysis
from skill_analysis_Parsa_Siri import run_skill_analysis
from salary_analysis_zain_alsaleh import run_salary_analysis
from AI_Exposure_index_Hussin_Rashwan import run_ai_exposure_index
from Data_Summary_Aymen import run_data_summary
from risk_analysis_med_ali import run_risk_analysis
from jobs_by_keyword_Fatah import run_jobs_by_keyword

#Print main menu function
def print_main_menu():
    print("\n" + "="*50)
    print("        AI IMPACT ON JOBS - MAIN MENU")
    print("="*50)
    print("1. Salary Analysis           |")
    print("2. Automation Risk Analysis  |")
    print("3. Growth vs Risk Analysis   |")
    print("4. Search by Skill           |")
    print("5. AI Exposure Index         |")
    print("6. Jobs by Keyword           |")
    print("7. Data Summary              |")
    print("8. Exit                      |")
    print("="*50)

def print_main_menu():
    print("\n" + "="*50)
    print("        AI IMPACT ON JOBS - MAIN MENU")
    print("="*50)   
    
    print("5. AI Exposure Index         |")
    print("2. Automation Risk Analysis  |")    
    print("7. Data Summary              |")    
    print("3. Growth vs Risk Analysis   |")   
    print("6. Jobs by Keyword           |")
    print("1. Salary Analysis           |")
    print("4. Search by Skill           |")
    print("8. Exit                      |")
    print("="*50)


#Main menu loop
def main_menu():
    while True:
        print_main_menu()
        choice = input("Enter your choice (1-8): ").strip()

        if choice == '1':
            run_ai_exposure_index()
        elif choice == '2':
            run_risk_analysis()
        elif choice == '3':
            run_data_summary()
        elif choice == '4':
            run_growth_vs_risk_analysis()
        elif choice == '5':
            run_jobs_by_keyword()
        elif choice == '6':
            run_salary_analysis()
        elif choice == '7':
            run_skill_analysis()
        elif choice == '8':
            print("\nExiting program. Goodbye! 👋")
            break
        else:
            print("\nInvalid input. Please enter a number from 1 to 8.\n")

if __name__ == "__main__":
    main_menu()