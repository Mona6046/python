#Divisors list
num=int(input("Enter the number : "))
numlist=list(range(1,num+1))
divisorList=[]
counter=0
flag=False
for number in numlist:
    if(num %number==0):
        counter+=1
        if(counter>2):
            flag=True
            break
        
            
if(flag):
    print("Its not a prime number")
else:
    print("Its a prime number")

