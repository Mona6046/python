#list the commom element in two list
#generate list 1
import random

#random list size
size1=random.randint(10,20)
size2=random.randint(10,20)

#generate random list
list1=random.sample(range(20),size1)
list2=random.sample(range(3,20),size2)


#print list
print(list1)
print(list2)

#declare a set to make sure there are unique value

finalList=set([num1 for num1 in (list1)  if num1 in list2 ])

#convert the set back to list
print(list(finalList))
