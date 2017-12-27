#list the commom element in two list
#generate list 1
import random

#random list size
size1=random.randint(10,20)
size2=random.randint(10,25)

#constant list 
list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#generate random list
list1=random.sample(range(20),size1)
list2=random.sample(range(3,20),size2)

#print list
print(list1)
print(list2)

#declare a set to make sure there are unique value
finalList=set([])

for num1 in list1:
    #check for number from list1 if present in second list
    if num1 in list2:
        finalList.add(num1)

#convert the set back to list
print(list(finalList))