# String slicing in Python to rotate a string

'''
In this tutorial, you will learn to rotate a string in Python using slicing. Strings in Python are a sequence of characters. Slicing is the process of accessing a 
part or a subset of a given string. For a given string of size n, ** we have to rotate the string by d elements ** . Where d is smaller than or equal to the size of the string. 
A string can be rotated clockwise (right rotation) or anticlockwise (left rotation). We will perform both rotations and give output for both rotations in our program.

Look at the examples to understand the input and output format.

Input:
s="studytonight"
d=3
Output:
Left Rotation : dytonightstu
Right Rotation : ghtstudytoni

To solve this, we will be using the concept of slicing in Python. Slicing will be used to divide the string into two parts.

For Left rotation, we will store the characters from the index 0 to d in the first part and the remaining characters in the second part.
For Right rotation, we will store the characters from the index 0 to (n-d) where n is the size of the string and the remaining characters in the second part.
Now we will join the second and first part as second + first for both rotations.


'''


# left rotation
def leftRotationBySLicing (myStr, d):
    str1 = myStr[0:d] # 0 to d-1 charcter will be extracted and assigned to str1 : ab
    str2 = myStr[d:] # d to len(myStr)-1   : cdef
    finalStr = str2+str1  # cdef + ab ==> cdefab
    print(f"FInal Right Rotation: by {d} postion : {finalStr}")


#  Right rotation
def rightRotationBySLicing(myStr, d):
    str1 = myStr[-d::] # [-2:len(myStr):1 ] ====> -2 -1 OR it could be like this [len(myStr)-d : ] :  ef
    print("Took Str From END: ",str1)
    str2 = myStr[0:len(myStr)-d] # len(myStr)-d  this will not let take d number of character   :  abcd
    print("Took Str From Start-D: ",str2)
    finalStr = str1+str2 # ef + abcd ==> efabcd
    print(f"FInal Right Rotation: by {d} postion : {finalStr}")

#  USE this below Approach in this no need to make any new array or String : it will be in Constat Space complexity 1 and time O(n)
# https://github.com/THENHKHAN/BasicProgramPracticeUsingPython/blob/main/5-ArraySpecificQuestIMP/5_RotateArrReversalALGO.py

myStr1 = "abcdef" # string are immutable so we can't assing value at their existing index Or can't replace its character: We;ll got ERROR: TypeError: 'str' object does not support item assignment
position = 2
print("My Orignal String:  " , myStr1)
print("*******************    LEFT Roataion By Slicing and + operator              *********************")
leftRotationBySLicing(myStr1, position)
myStr2 = "abcdef"
print("My Orignal String:  " , myStr1)
print("*******************    RIGHT Roataion By Slicing and + operator              *********************")
rightRotationBySLicing(myStr2, position)