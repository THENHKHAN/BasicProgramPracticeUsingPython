# Python Program to Check if a given string is a binary string or not
'''
In this tutorial, you will learn to check if a given string is a binary string or not in Python. Strings in Python are a sequence of characters wrapped in single, double, 
or triple quotes. 
Def :-> Binary strings are the strings that have characters either 1 or 0. If there is any character that is not 1 or 0, then the string is a non-binary string.

Let us look at the sample input and output of the program.

Input: "010010"
Output: binary

Input: "001120001"
Output: non-binary

To solve this problem in Python we can follow these approaches:

--> set approach
--> iterative approach
'''

# method-1 : iterative approach
def iterativeApproach(myStr): # binary="01" we can also take thing and check chacarter from given string they belong to this or not if not then retunr false
    for i in range(len(myStr)):
        if (myStr[i] != "0" and myStr[i] != "1") :
            return False
    
    return True

# method-2 :  set approach : here time saved but extra space
def setApproach(myStr):
    b = set(myStr)
    print(b) # {'1', '0'}
    mySet = {'1', '0'}
    if mySet == b or b == {'0'} or b == {'1'}: # since set will removed the duplicate 
        return True
    else:
        return False

string="010010"
# string= "001120001"

print("\n **************  Method-1 iterative approach *********************\n ")  
print("The original string is : " , string)
print("Does ", string , "Binary string? : ", "Yes, Binary string" if iterativeApproach(string) else  "No, not a Binary string")


print("\n **************  Method-2  set approach *********************\n ")  
print("The original string is : " , string)
print("Does ", string , " Binary string? : ", "Yes, Binary string" if setApproach(string) else  "No, not a Binary string")






'''
 **************  Method-1 iterative approach *********************

The original string is :  010010
Does  010010 Binary string? :  Yes, Binary string

 **************  Method-2  set approach *********************

The original string is :  010010
{'1', '0'}
Does  010010  Binary string? :  Yes, Binary string
'''