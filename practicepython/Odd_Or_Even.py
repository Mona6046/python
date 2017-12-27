#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

def checkInputNumeric(number,message):
    returnValue=""
    if(number.isnumeric()):
        returnValue=number
    else:
        print("This is not a numeric value.Please enter the value again")
        userAge = input(message)
        returnValue=checkInputNumeric(userAge,message)
    return returnValue

message="Please enter a number: " 
number = input(message)
number=int(checkInputNumeric(number,message))
if(number%2==0):
    print("The number is even")
else:
    print("The number is odd")

message2="Please enter a number to divide first number: " 
number2 = input(message)
number2=int(checkInputNumeric(number2,message2))
try:
    if(number%number2==0):
        print("{} divides {} evenly".format(number2, number))
    else:
        print("{} doesnot divides {} evenly".format(number2,number))
except ZeroDivisionError:
    print("Oops!  zero no valid number.  Try again...")
