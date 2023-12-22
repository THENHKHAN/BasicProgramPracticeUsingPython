# Python program for largest Element In an Array/List

'''
we will learn how to find and display the largest element in an array using the Python programing language. 
We will be using the concept of loop and conditional statements in this tutorial.
'''
# Python array FROM array module 
'''
Python arrays are data structures that store homogenous data. Arrays stores objects of the same datatype. Arrays are mutable, meaning that the data in an array can be changed and iterative, 
meaning each element in an array can be accessed one by one.
In python, you need to import the array module to create an array. The array(data_type, value) function is used to specify an array with its data type and value list 
given as arguments. Look at the example given below for creating an array in Python.
import array as ar
a = ar.array('i', [1, 2, 3, 4, 5])
Here we have declared an array of integer type with the value list [1, 2, 3, 4, 5]. The letter i is a type code. This determines the type of the array during creation.
'''

import array as arr
# Method-1 : using max() function

def usingMaxFun(myArr) :
    return max(myArr)


# Method-2 : Using loop and condition
def usingLoopAndCondition(myArr) :
    # let max element is the element wihch is on index 0
    maxEle = myArr[0]
    for ele in myArr:
        if ele >= maxEle :
            maxEle = ele
        else:
            pass
    else:
        return maxEle

def findSecLargestEle(myArr):
    maxSecLargEle = myArr[0]
    firstMaxElem = max(myArr)
    for ele in myArr :
        if (ele >= maxSecLargEle) and (ele != firstMaxElem):
            maxSecLargEle = ele       
    else:
        return maxSecLargEle




#input values 
a = arr.array('i',[3, 24, 11, 2])
print(f"my Array : {a}" )
print("*********************   WAY - 1 : By using max() function ***********************")
print(f" Greatest element in the array is: {usingMaxFun(a)}")

print("*********************   WAY - 2 : By Using loop and condition ***********************")
print(f" Greatest element in the array is: {usingLoopAndCondition(a)}")

print("*********************   WAY  : By Using max(), loop and condition find 2nd Largest element ***********************")
print(f" Greatest element in the array is: {findSecLargestEle(a)}")


#  I/O:
'''
my Array : array('i', [3, 24, 11, 2])
*********************   WAY - 1 : By using max() function ***********************
 Greatest element in the array is: 24
*********************   WAY - 2 : By Using loop and condition ***********************
 Greatest element in the array is: 24
*********************   WAY  : By Using max(), loop and condition find 2nd Largest element ***********************
 Greatest element in the array is: 11

'''