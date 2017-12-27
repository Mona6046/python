#Reverse Word Order
# print my name is mona to mona is my name

#input string 
string=input("Enter the string : ")

#split string based on space
splitString=string.split(" ")

#reverse words
reversesplitString=splitString[::-1]

#join list of words in string
output=result = " ".join(reversesplitString)

#print string
print(output)