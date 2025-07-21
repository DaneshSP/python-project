while True:
    try:
        import random
        choice=["rock","paper","scissor"]
        computer_num=random.randint(0,2)
        computer_choice=choice[computer_num]

        user_num=int(input("1:rock\n2:paper\n3:scissor\n4:Exit\nenter your choice: "))
        
        if user_num == 4:
            print("You are exiting from the game")
            break
        user_choice=choice[user_num-1]
        print("your choice: " +user_choice)
        
        if user_choice==computer_choice:
            print("match drow")
            
        elif user_choice == "rock" and computer_choice =="scissor":
            print("you win")
        
        elif user_choice == "paper" and computer_choice == "rock":
            print("you win")
            
        elif user_choice == "scissor" and computer_choice == "paper":
            print("you win")
        else:
            print("you lose")
            
    except:
        print("enter profer choice only")