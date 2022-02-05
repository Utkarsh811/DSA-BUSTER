import random
rock=  "✊"
paper= "🤚"
scissor= "✌"
game_list=[rock,paper,scissor]
user_choice=int(input("What you want to choose? type 0 for rock ,1 for paper or 2 for scissor.\n"))
print(game_list[user_choice])
computer_choice=random.randint(0,2) 
print("computer_choice")
print(game_list[computer_choice])
if user_choice>=3 or user_choice<0:
    print("You choose invalid number. You lose")
elif user_choice==0 and computer_choice==2:
    print("You win")
elif computer_choice==0 and user_choice==2:
    print("You lose")        
elif user_choice>computer_choice:
    print("You win")
elif computer_choice>user_choice:
    print("You lose")
elif computer_choice==user_choice:
    print("It's a draw")