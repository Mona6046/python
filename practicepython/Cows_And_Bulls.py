import random

def checkwin(number,guessNumber):
    if(number==guessNumber):
        return True
    else:
        return False

def cowbull(number,guessNumber):
    cowbull=[0,0]
    for i in range(0,len(number)):
        if(guessNumber[i]in number):
            if(number[i]==guessNumber[i]):
                cowbull[0]+=1
            else:
                cowbull[1]+=1
    return cowbull

number=str(random.randint(1000,9999))
count=0
guessNumber=0
while guessNumber!="exit":
    guessNumber=input("Guess four digit number")
    if(guessNumber=="exit"):
        break
    count+=1
    if(checkwin(number,guessNumber)):
        print("Congrats you guess correct number.The correct number was {}\n".format(number))
        print("you took {} number of chances\n".format(count))
        break
    cowbullvar=cowbull(number,guessNumber)
    print("you have got {} cows and {} bulls".format(cowbullvar[0],cowbullvar[1]))




    