#Ask the user for a string and print out whether this string is a palindrome or not


def isPalandrome(string):
    #reverse String
    reverseString=string[::-1]
    if(string==reverseString):
        return True
    return False

#ask for input string 
inputString=input("Enter the string :")
flag=isPalandrome(inputString)

if(flag==True):
    print ("String is palindrome")
else:
    print ("String is not palindrome")


