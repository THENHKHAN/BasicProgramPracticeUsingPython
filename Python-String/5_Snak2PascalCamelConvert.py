# PROGRAM:-->  Python Convert Snake case to Pascal case and camelCase
# Def:
'''
Snake case:-> Snake case contains compound words or phrases in which words are separated using one underscore (“_”) and no spaces, with each word’s initial 
letter usually in lowercase within the phrase or compound. Like in “study_tonight” and “Study_tonight”.

Pascal case:-> In the pascal case, the first letter of each word in a phrase or a compound is always a capital letter. Without any 
space between the words. Like in “StudyTonight” and “HelloWorld”. For example,

'''
from string import capwords # capwords function make all the word's first letter capital

# Method-1 
def usingCapWordsFunction (Snake_case) :

    # 1st we have replace _ with " " so that we can  use capwords
    rmv_ = Snake_case.replace("_", " ")
    # now we can use capwords to make each word's first letter capital
    pascal = capwords(rmv_)
    # now we have to remove space 
    actualPascal = pascal.replace(" " , "")
    print(f"snake case {Snake_case} To Pascal case : {actualPascal}")

# Method-2 
def usingTitleFunction (Snake_case) : # 
    # we will use the title() function of the String class which returns the string after capitalizing the first character of every word in the string. To remove underscore and spaces from the string we will use another string function replace().
    #1- remove _ 1st 
    rmv_ = Snake_case.replace("_" , " ")
    #2- make each word 1st letter upper case
    pascal = rmv_.title()
    #3- remove space b/w the words
    actualPascal = pascal.replace(" " , "")
    print(f"snake case {Snake_case} To Pascal case : {actualPascal}")

def snakeCamelCase ( Snake_case ) :
    #1- rmv _ 1st
    rmv_ = Snake_case.replace("_" , " ")
    #2- make each word's 1st character upperCase
    camelTemp = capwords(rmv_) 
    #3- remv sapce 
    pascal = camelTemp.replace(" " , "")
    #4- make the 1st letter of the string lower: we'll use kth character lower case 
    k=0 # index of which we want to make lower case
    camelCase = pascal[k].lower() + pascal[k+1: ]
    print(f"snake case {Snake_case} To Pascal case : {camelCase}")



Snake_case = input("Input snake case string (like- Study_tonight) :  " )

print("********** Using capwords() String function :snake_case->SnakeCase   *************")
usingCapWordsFunction (Snake_case)

print("********** Using title() String method  :snake_case->SnakeCase   *************")
usingTitleFunction (Snake_case) 

print("********** Using capwords() String method :  Snake->camelCase   *************")
snakeCamelCase ( Snake_case )



# Approach
'''
To solve this problem, there are several different approaches, some of them are-

1-> Using capwords() 
2-> Title() and replace()
'''

# more 
'''
Approach 1: capwords()
In this approach, we will use the capwords() function from the string class. This function is used to capitalize all the words in the string. To capitalize the first letter of each word we have used this function. 
Also, we need to remove any underscore (“_”) or spaces which can be done by using the replace function.

'''

# I/O
'''

Input: python_language

Output: PythonLanguage

Input: Hello_world

Output: HelloWorld

'''

#More Info  : PascalCase and camelCase Diff
'''
Pascal case is similar to camel case. The only difference between the two is that pascal case requires the first letter of the first word to also be capitalized. 
So, when using pascal case, every word starts with an uppercase letter (in contrast to camel case, where the first word is in lowercase).
'''

