test = True
while test:

    prompt = "*** Ai Impact on jobs ***"
    prompt += "\n1. Salary Analysis"
    prompt += "\n2. Automation Risk Analysis"
    prompt += "\n3. Growth vs Risk Comparision"
    prompt += "\n4. Search by skill"
    prompt += "\n5. Exit"
    prompt += "\n"

    answer = input(prompt)
    if answer == 1 :
        print('Go To Salary Analysis Feature') 
    
    if answer == 2 :
        print('Go To Automation Risk Analysis Feature') 

    if answer == 3 :
        print('Go To Growth vs Risk Analysis Feature') 

    if answer == 4 :
        print('Go To Search by skill Feature') 

    if answer == 5 :
        print('Exiting')
        test = False

    print(answer) 
