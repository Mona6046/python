#Guessing Game One
#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

import random
# generate random number
randomNum=random.randint(1,9)

#user input number
counter=0
while (quit):
    userNum=input("Guess the number between [1-9] including (1,9)")
    if(userNum!="exit"):
        counter+=1
        if(randomNum>int(userNum)):
            print("Guessed value is too lower than actual")
        elif(randomNum<int(userNum)):
            print("Guessed value is too higher than actual")
            print("!Guess again or type exit")
        else:
            print("correct guess.the random number was {} \n".format(randomNum))
            print("and you guess the correct result in {} chances \n".format(counter))
            break
    else:
        break

print("Game Over!!")