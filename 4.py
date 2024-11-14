print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
import random
number=int(input())
print("\n**********************\n")
if(number==0):
    print("You choose Rock!")
elif(number==1):
    print("You choose Paper!")
elif(number==2):
    print("You choose Scissor!")
else:
    print("INVALID CHOICE!!")
    exit()
comp=["rock","paper","scissor"]
no=random.randint(0,2)
if(no==0):
    print("Computer choose Rock!")
elif(no==1):
    print("Computer choose Paper!")
elif(no==2):
    print("Computer choose Scissor!")
else:
    print("INVALID CHOICE!!")
    exit()
print("\n***********************\n")
if(number==no):
    print("Its a Draw")
elif((number==1 and no==0) or(number==0 and no==2) or (number==2 and no==1)):
    print("you win!!")
else:
    print("you Lose!!")