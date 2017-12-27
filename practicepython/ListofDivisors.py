#Divisors list
num=int(input("Enter the number : "))
numlist=list(range(1,num+1))
divisorList=[]
for number in numlist:
    if(num %number==0):
        divisorList.append(number)
print(divisorList)
