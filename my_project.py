import random

list=["snake","water","gun"]

x=input("choose one option from snake, water or gun:\n")

y = random.choice(list)

print("python's choice is: ",y)

def snake_water_gun(a,b):

    if a==b:
        return None

    # if computer choose water then all possibilities
    if b=="water":
        if a=="gun":
            return False
        elif a=="snake":
            return True

    # if computer choose gun then all possibilities
    elif b=="gun":
        if a=="water":
            return True
        elif a=="snake":
            return False

    # if computer choose snake then all possibilities
    elif b=="snake":
        if a=="water":
            return False
        elif a=="gun":
            return True


winner = snake_water_gun(x,y)
if winner==None:
    print("The game is a tie !")
elif winner:
    print("congartulation !, you are a winner.")
else:
    print("you lose !, python is the winner.")