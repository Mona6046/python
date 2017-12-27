#List Comprehensions
#Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.


list1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#comphrehensive way of writing for to append in new list
evenlist=[a for a in list1 if a%2==0 ]

print(evenlist)
