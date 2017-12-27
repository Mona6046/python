#List Less Than Ten Solutions

def checkInputNumeric(number,message):
    returnValue=""
    if(number.isnumeric()):
        returnValue=number
    else:
        print("This is not a numeric value.Please enter the value again")
        userAge = input(message)
        returnValue=checkInputNumeric(userAge,message)
    return returnValue

listNumber = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
message="Please enter a number: " 
number = input(message)
number=int(checkInputNumeric(number,message))
new_list=[]
for num in listNumber:
    if num<number:
        new_list.append(num)
print(new_list)
