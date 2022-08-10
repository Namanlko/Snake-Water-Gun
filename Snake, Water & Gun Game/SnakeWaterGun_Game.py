# Snake, Water and Gun Game.

'''
We all have played a Snake, Water and Gun game in our childhood. If you haven't just google the rules of this game and write a python program capable of playing this game with the user.
'''

import random

def Game(comp,you):
    if(comp == you):
        return None
    
    elif(comp == 's'):
        if(you == 'g'):
            return True
        else:
            return False

    elif(comp == 'w'):
        if(you == 's'):
            return True
        else:
            return False
    
    elif(comp == 'g'):
        if(you == 'w'):
            return True
        else:
            return False
    
print("Computer's Turn Choose Snake(s), Water(w) and Gun(g):")
randNo = random.randint(1,30)

if (randNo >= 0 and randNo <= 10):
    comp = 's'
elif (randNo > 10 and randNo <= 20):
    comp = 'w'
else:
    comp = 'g'

you = input("Your's Turn Choose Snake(s), Water(w) and Gun(g):")

r = Game(comp,you)

if(r == None):
    print("You Choose:",you)
    print("Computer Choose:",comp)
    print("Match is Draw!")

elif(r == True):
    print("You Choose:",you)
    print("Computer Choose:",comp)
    print("You Win!")

else:
    print("You Choose:",you)
    print("Computer Choose:",comp)
    print("Computer Win!")