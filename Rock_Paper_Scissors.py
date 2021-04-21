import random

user_name = input("Enter you Name : ")

while True:
    print(" Make Selection ")
    print("1. Rock,\n2. Scissors\n3. Paper")

    user_input = int(input("Enter the number : "))
    
    while user_input>3 or user_input <1:
        user_input = int(input("Please Enter your choice between 1-3 : "))

    if user_input == 1:
        user_input_choice = 'Rock'

    elif user_input == 2:
        user_input_choice = 'Scissors'

    elif user_input == 3:
        user_input_choice = 'Paper'

    print('Hey',user_name,'!','You have Selected : ',user_input_choice)

    device_input = random.randint(1,3)

    if device_input == 1:
        device_input_choice = 'Rock'

    elif device_input == 2:
        device_input_choice = 'Scissors'

    elif device_input == 3:
        device_input_choice = 'Paper'

    print('Hey',user_name,'!','Your opponent Selected : ',device_input_choice)

    if user_input ==1:

        if device_input == 2:
            print("Rock wins the match")
            result = "Rock"

        elif device_input == 3:
            print("Paper wins the match")
            result = "Paper"

        elif device_input == 1:
            print("It's a Draw")
            result = "Draw"

    elif user_input ==2:

        if device_input == 1:
            print("Rock wins the match")
            result = "Rock"

        elif device_input == 3:
            print("Scissors wins the match")
            result = "Scissors"
            
        elif device_input == 2:
            print("It's a Draw")
            result = "Draw"

    elif user_input ==3:

        if device_input == 1:
            print("Paper wins the match")
            result = "Paper"

        elif device_input == 2:
            print("Scissor wins the match")
            result = "Scissors"
            
        elif device_input == 3:
            print("It's a Draw")
            result = "Draw"
    if result == "Draw":
        print("Hard Match! Retry?")
    else:
        if user_input_choice == result:
            print("Yeah!",user_name,'You won the match.')
        else:
            print("You Loss!",user_name)
    print("Wanna Play Again?")
    print("Y for Yes and N for No")
    rematch = input()
    if rematch =='n' or rematch == 'N':
        break
    print("Thank you for Playing",user_name)

