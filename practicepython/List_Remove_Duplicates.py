#List Remove Duplicates without sets

list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list=[]
for num in list1:
    if num not in new_list:
        new_list.append(num)

print(new_list)

