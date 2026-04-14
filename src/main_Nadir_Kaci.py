# main.py

# Import Growth vs Risk Analysis feature
from growth_analysis_Nadir_Kaci import growth_vs_risk_menu
from skill_analysis_Parsa_Siri import run_skill_analysis
from salary_analysis_zain_alsaleh import run_salary_analysis
from AI_Exposure_index_Hussin_Rashwan import run_ai_exposure_index

def print_main_menu():
    print("\n" + "="*50)
    print("        AI IMPACT ON JOBS - MAIN MENU")
    print("="*50)
    print("1. Salary Analysis           [Implemented]")
    print("2. Automation Risk Analysis  [Coming Soon]")
    print("3. Growth vs Risk Analysis   [Implemented]")
    print("4. Search by Skill           [Implemented]")
    print("5. AI Exposure Index         [Coming Soon]")
    print("6. Jobs by Keyword           [Coming Soon]")
    print("7. Exit")
    print("="*50)

def main_menu():
    while True:
        print_main_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == '1':
            run_salary_analysis()
        elif choice == '2':
            print("\nAutomation Risk Analysis feature not implemented yet.\n")
        elif choice == '3':
            growth_vs_risk_menu() 
        elif choice == '4':
            run_skill_analysis()
        elif choice == '5':
            run_ai_exposure_index(data)
        elif choice == '6':
            print("\nJobs by Keyword feature not implemented yet.\n")
        elif choice == '7':
            print("\nExiting program. Goodbye! 👋")
            break
        else:
            print("\nInvalid input. Please enter a number from 1 to 7.\n")

if __name__ == "__main__":
    main_menu()