#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

def checkInputNumeric(number,message):
    returnValue=""
    if(number.isnumeric()):
        returnValue=number
    else:
        print("This is not a numeric value.Please enter the value again")
        userAge = input(message)
        returnValue=checkInputNumeric(userAge,message)
    return returnValue

userName = input("Please enter your name: " )
userAge = input("Please enter your age: ")
age=checkInputNumeric(userAge,"Please enter your age: ")
yearfor100=100-int(age)
message="Hey ,you will be celebrating your 100th birthday after " + str(yearfor100) + " years \n"
print(message)
repeatNumber = input("Please enter your the number you want the above message to be repeted: ")
number=checkInputNumeric(repeatNumber,"Please enter your the number you want the above message to be repeted: ")
print((message ) *int(number))








