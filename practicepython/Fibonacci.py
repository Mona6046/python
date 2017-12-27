#Fibonacci 
#length of Fibonacci series

length=input("Enter the length of Fibonacci series")
series=[]
def nextFibonacci(lastNumber,secondLastNumber):
    return lastNumber+secondLastNumber
lastNumber=1
secondLastNumber=0
count=0
while(count<int(length)):
    series.append(lastNumber)
    temp=nextFibonacci(lastNumber,secondLastNumber)
    secondLastNumber=lastNumber
    lastNumber=temp
    count+=1

print(series)