import random
print("Lets Play Rock Paper Scissor")
print("There are 5 set in one Series")
print("Points for Win,Tie,Lose are 20,10,00 resp.")
computer_score=0
user_score=0
print("Your Score:",user_score)
print("Computer Score:",computer_score)
for x in range(1,6):
    alist=["Rock","Paper","Scissor"]
    b=random.choice(alist)
    print("Set", x)
    user_inp=str(input("Enter your choice:"))
    user_input=="Rock" or user_input==Paper or user_input==Scissor
    print("Computer choice:",b)
    if b==user_inp:
        print("Tie")
        computer_score+=10
        user_score+=10
        print("Computer Score after set",x,"=",computer_score)
        print("Your Score after set",x,"=",user_score)
    elif b=="Rock" and user_inp=="Scissor":
        print("You lose this set")
        computer_score+=20
        print("Computer Score after set",x,"=",computer_score)
        print("Your Score after set",x,"=",user_score)    
    elif b=="Paper" and user_inp=="Rock":
        print("You lose this set")
        computer_score+=20
        print("Computer Score after set:",x,"=",computer_score)
        print("Your Score after set",x,"=",user_score)
    elif b=="Scissor" and user_inp=="Paper":
        print("You lose this set")
        computer_score+=20
        print("Computer Score after",x,"=",computer_score)
        print("Your Score after set",x,"=",user_score)
    else:
        print("Yow win this set")
        user_score+=20
        print("Computer Score after set",x,"=",computer_score)
        print("Your Score after set",x,"=",user_score)            
if user_score==computer_score:
    print("Series Tie")
elif user_score>computer_score:
    print("You win the series")
else:
    print("You lose the series")
print("Your Final Score:",user_score)
print("Computer Final Score:",computer_score)      
    
