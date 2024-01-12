# Python program to check if a string is palindrome or not

'''
A string is said to be palindrome if a string is read the same way as its reverse. For example- madam is a palindrome as the reverse of this string is also madam.
For a given string our program should check and return Yes if the string is a palindrome and No if the string is not a palindrome. For example,

Input: cricket
Output: No

Input: level
Output: Yes
'''

def checkNPrint(check:bool):
     if check:
        print(f"Yes, {string} is Palindrome")
     else:
        print(f"No, {string} is not palindrome")
     

# method-1
def isPalindrom(myStr):
       newStr = reversed(myStr)  # <reversed object at 0x000001F6B36FBE50>
    #    for s in newStr:
    #         print(s, end=" ") # t e k c i r c
       s = "".join(newStr) 
    #    print(s)
       if myStr == s :
            return True
       else:
            False

# method-2
#  much better than above since it creating only srtring but above is two.
def isPalindromBySlicing(myStr):
    #  newStr = myStr[::-1] # it will give from last to start since -1 is used to nmake the flow reverse.
    #  print(newStr)
    #  if newStr == myStr :
     if myStr == myStr[::-1] :
        return True
     return False
     

# method-3 : The iterative method of checking each character in the string # Here we DONT HAVE TO MAKE ANY NEW STRING -- MUCH BETTER THAN ABOVE TWO
def isPalindrombyCheckingEachChar(myStr):
     start , end = 0, len(myStr)-1
     for ind in range(0,int(len(myStr)/2)):
          if myStr[start] != myStr[end] : #  it could also be  - myStr[ind] != myStr[len(myStr)-ind-1]  - to avoid two new variables
                return False
          start += 1 # incrementing start index 
          end -= 1 # decremeneting end index
     else:
        return True



string=  "Level" #  cricket,madam. nitin
print("*********   Method-1 By using reversed() funciton and join()   **********************")
checkNPrint(isPalindrom(string.lower()))

print("*********   Method-2 By using SLICING to reverse the string   **********************")
checkNPrint(isPalindromBySlicing(string.lower()))

print("*********   Method-3 By using iterative method of checking each character in the string   **********************")
checkNPrint(isPalindrombyCheckingEachChar(string.lower()))


#  INPUT/OUTPUT: 
# for ignoring case sensitivity i used lower() method to make the string lower then compare.

'''
*********   Method-1 By using reversed() funciton and join()   **********************
Yes, Level is Palindrome
*********   Method-2 By using SLICING to reverse the string   **********************
Yes, Level is Palindrome
*********   Method-3 By using iterative method of checking each character in the string   **********************
Yes, Level is Palindrome
'''