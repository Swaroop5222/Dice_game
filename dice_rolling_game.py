#Dice rolling game

import random

def number_6_dice(): 
    while(True):
        ask=input('Do you want to roll dice?(y/n): ')
        if ask=='y':
            dice1=random.randint(1,6)
            dice2=random.randint(1,6)
            print("After Rolling dice1: ",dice1)
            print("After rolling dice2: ",dice2)
        elif ask=='n':
            return -1
        else:
            print("Enter either 'y' or 'n' to continue")

def number_12_dice(): 
    while(True):
        ask=input('Do you want to roll dice?(y/n): ').lower()
        if ask=='y':
            dice1=random.randint(1,12)
            dice2=random.randint(1,12)
            print("After Rolling dice1: ",dice1)
            print("After rolling dice2: ",dice2)
        elif ask=='n':
            return -1
        else:
            print("Enter either 'y' or 'n' to continue")

print('Choose either 6-numbered dice or 12-numbered dice')

while(True):
    choice=int(input('Enter 6 for 6 numbered dice and 12 for 12 numbered dice: '))
    if choice==6:
        end=number_6_dice()
        if end==-1:
            break
    elif choice==12:
        end=number_12_dice()
        if end==-1:
            break
    else:
        print('Enter valid number to choose the dice(6 or 12 only)')
        
print("Game Completed.Hope you enjoyed")

    
