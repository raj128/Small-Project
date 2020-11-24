print("Guess the number between 1 to 50")
print("You have only 5 attempt")
import random
guess=random.randint(1,50)
print(guess)
"""for x in range(1,5):
    a=int(input("Enter the number="))
    if a==guess:
        print("congrulation")
        break
    elif a>=guess:
        print("your number is large")
    else:
        print("your number is small")"""
turn=0
while turn<5:
     a=input("Enter the number:")
     b=a.isdigit()
     if b==True:
         a=int(a)
         if a==guess:
             print("congrulation")
             break
         elif a>guess and a<51:
             print("your number is large")
             turn+=1
         elif a<guess and a>0:
             print("your number is small")
             turn+=1
         else:
             print("Enter the integer less than 51")  
     else:
         print("Enter the integer no like 7,24,42 etc")


