"""
1 for snake 
-1 for water
0 for gun 

"""

import random

computer = random.choice([1,0,-1])

yourstr=input("enter your choice : ")

youdict={"s":1,"w":-1,"g":0}

reversedict={1:"snake",-1:"water",0:"gun"}

you =youdict[yourstr]

print(f"you have chosen {reversedict[you]} \n and computer chose {reversedict[computer]}  ")

if(you==computer):
    print("draw match")

else:
    if(computer==1 and you==-1):
        print("computer wins")

    elif(computer==-1 and you==0):
        print("computer wins")
    
    elif(computer==0 and you==1):
        print("computer wins")

    elif(you==1 and computer==-1):
        print("you win")

    elif(you==-1 and computer==0):
        print("you wind")

    elif(you==0 and computer==1):
        print("you win")


