#Dice rolling game

import random

while(True):
    ask=input('Do you want to roll dice?(y/n): ')
    if ask=='y':
        dice1=random.randint(1,6)
        dice2=random.randint(1,6)
        print("After Rolling dice1: ",dice1)
        print("After rolling dice2: ",dice2)
    elif ask=='n':
        break
    else:
        print("Enter either 'y' or 'n' to continue")
        
print("Game Completed.Hope you enjoyed")

    
