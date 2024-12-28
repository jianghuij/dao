import random
while 1:
    to = 6
    print("new game,press 'enter' to start ")
    while 1:
        text=str(to)+" round left:"
        end=input(text)
        ran = random.randint(1, to)
        if to==ran:
            print("bad,your lose!")
            print("-------------------------------")
            break
        else:
            print("luck,continue!")
        to-=1


