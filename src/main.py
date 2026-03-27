from data_loader import DataLoader
from skill_analysis import run_skill_analysis

loader = DataLoader()
data = loader.load_data()

test = True
while test:
    print()
    prompt = "*** Ai Impact on jobs ***"
    prompt += "\n1. Salary Analysis"
    prompt += "\n2. Automation Risk Analysis"
    prompt += "\n3. Growth vs Risk Comparision"
    prompt += "\n4. Search by skill"
    prompt += "\n5. AI Exposure Index"
    prompt += "\n6. Jobs by Keyword"
    prompt += "\n7. Exit"
    prompt += "\n"

    answer = input(prompt + "Please enter an option (1-7): ")

    if answer == '1':
        print('Go To Salary Analysis Feature')

    elif answer == '2':
        print('Go To Automation Risk Analysis Feature')

    elif answer == '3':
        print('Go To Growth vs Risk Analysis Feature')

    elif answer == '4':
        run_skill_analysis(data)

    elif answer == '5':
        print('Go To AI exposure index')

    elif answer == '6':
        print('Go To Jobs By Keyword')

    elif answer == '7':
        print('Exiting')
        test = False

    else:
        print("Invalid option.")