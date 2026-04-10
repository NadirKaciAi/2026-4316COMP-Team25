# main.py

# Import Growth vs Risk Analysis feature
from growth_analysis_Nadir_Kaci import growth_vs_risk_menu  

def print_main_menu():
    print("\n" + "="*50)
    print("        AI IMPACT ON JOBS - MAIN MENU")
    print("="*50)
    print("1. Salary Analysis           [Coming Soon]")
    print("2. Automation Risk Analysis  [Coming Soon]")
    print("3. Growth vs Risk Analysis   [Implemented ]")
    print("4. Search by Skill           [Coming Soon]")
    print("5. AI Exposure Index         [Coming Soon]")
    print("6. Jobs by Keyword           [Coming Soon]")
    print("7. Exit")
    print("="*50)

def main_menu():
    while True:
        print_main_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == '1':
            print("\nSalary Analysis feature not implemented yet.\n")
        elif choice == '2':
            print("\nAutomation Risk Analysis feature not implemented yet.\n")
        elif choice == '3':
            growth_vs_risk_menu() 
        elif choice == '4':
            print("\nSearch by Skill feature not implemented yet.\n")
        elif choice == '5':
            print("\nAI Exposure Index feature not implemented yet.\n")
        elif choice == '6':
            print("\nJobs by Keyword feature not implemented yet.\n")
        elif choice == '7':
            print("\nExiting program. Goodbye! 👋")
            break
        else:
            print("\nInvalid input. Please enter a number from 1 to 7.\n")

if __name__ == "__main__":
    main_menu()