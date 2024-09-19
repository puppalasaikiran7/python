import random

def game():

    print("lets play the game : ")
    score=random.randint(1,69)
    with open("D:\learning\python\chapter9_practiceset/highscore.txt")as f:
        highscore=f.read()

        if(highscore!=""):
            highscore=int(highscore)
        else:
            highscore=0
    
    if(score>highscore):
            with open("D:\learning\python\chapter9_practiceset/highscore.txt","w") as f:
                f.write(str(score))

    return score

value=game()
print(value)