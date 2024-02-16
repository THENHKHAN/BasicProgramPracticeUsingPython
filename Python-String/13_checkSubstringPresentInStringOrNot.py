# https://www.studytonight.com/python-programs/python-program-to-check-if-a-substring-is-present-in-a-given-string

# Python Program to Check if a Substring is Present in a Given String
'''
In this tutorial, we will learn to check if a substring is present in a given string or not. Strings in Python are data structures for 
storing characters in a sequence. A substring can be defined as a sequence of characters within another string.

In our program, for a given string and substring we will check if the substring is a part of the string or not and return the result 
accordingly. For example,

Input:

string="Python Language"
substring="thon"
Output: Yes

To solve this problem there are several different approaches, some of them are:

--> Using in operator
--> Using find()
--> Using contains()

'''

# method-1 Using Operator (in operator)
def usingOperator(myStr, subStr):
    if subStr in myStr:
      return "Yes"
    else:
        return "NO"

# method-2 using find method of string (str.find()):
    # find() is a built-in string function in the python library that returns the lowest index at which the substring occurs in the string. It will return -1 if the substring is not found. We will use this string method and check the value returned by this function to get the final result.
def usingFind(myStr, subStr):
       res = myStr.find(subStr)
       if res != -1:
             return "Yes"
       else:
            return "NO"
       
# method-2using find method of string (contains(str, patterns)):
# contains() method of an operator class. contains() function is used to test if a pattern of characters is contained within a string of a series. The function returns boolean values. To use the function we have to import the operator package in our program.
from operator import contains
def uisngOperatorContains(myStr, subStr):
       check = contains(myStr, subStr)
       if check:
             return "Yes"
       else:
            return "NO"

   
   

string="StudyTonight"
substring="Study"
print("\n **************  Method-1  in operator *********************\n ")  
print("The original string is : " , string)
print("Does ",substring," exist in ",string,"? : ", usingOperator(string, substring))

print("\n **************  Method-2  find() method *********************\n ")  
print("Does ",substring," exist in ",string,"? : ", usingFind(string, substring))

print("\n **************  Method-3 contains() method of operator *********************\n ")  
print("Does ",substring," exist in ",string,"? : ", uisngOperatorContains(string, substring))

'''
 **************  Method-1  in operator *********************

The original string is :  StudyTonight
Does  Study  exist in  StudyTonight ? :  Yes

 **************  Method-2  find() method *********************

Does  Study  exist in  StudyTonight ? :  Yes

 **************  Method-3 contains() method of operator *********************

Does  Study  exist in  StudyTonight ? :  Yes

'''

'''
 **************  Method-1  in operator *********************

The original string is :  StudyTonight
Does  StudyPP  exist in  StudyTonight ? :  NO

 **************  Method-2  find() method *********************

Does  StudyPP  exist in  StudyTonight ? :  NO

 **************  Method-3 contains() method of operator *********************    

Does  StudyPP  exist in  StudyTonight ? :  NO
'''