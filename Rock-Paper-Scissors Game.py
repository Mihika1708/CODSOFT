import random
print("Welcome to Rock-Paper-Scissors Game ")
#defining a variable to ask the user for another game
n="yes" 
while n=="yes":
    options=["rock","paper","scissors"]
    user_input=input("Choose rock , paper or scissors :")
    computer_selection=random.choice(options)
    if user_input==computer_selection:
        print("It's a tie")
    elif user_input=="rock" and computer_selection=="scissors":
        print("user wins")
    elif user_input=="scissors" and computer_selection=="paper":
        print("user wwins")
    elif user_input=="paper" and computer_selection=="rock":
        print("user wwins")
    else:
        print("Computer wins")
    print("the computer's choice was",computer_selection)
    n=input("Enter yes If you want to play another game")
    
print("Hope you enjoyed!!")
    