# Python program to print positive and negative numbers from a given list.

# Input: [2, 6, -10, -3, 1, -9]
# Output: [2, 6, 1]

# Input: [-2, -4, 5, -3, 0, 6, -10]
# Output: [5, 0, 6, ]

# Approach to print positive numbers in a list

'''To execute this task we can follow various approaches, which will be discussed in detail below

1---> Traversing the list and checking each element if it is positive
2---> Using list comprehension
3---> Using lambda functions
'''

# ----------- METHOD-1  ==  Traversal------------
def collectPositive(lst):
    posList = []
    for ele in lst :
        if (ele >= 0) :
            posList.append(ele)
    else:
        return posList

def collectNegative(lst):
    negList = []
    for ele in lst :
        if ele < 0 :
            negList.append(ele)
    else:
        return negList

# ----------- METHOD-2 ==  List comprehension ------------
def collectPositiveListComprehension(lst):
     posList = [ ele for ele in lst if ele >=0 ] # with else : ["Yes" if num % 3 == 0 else "No" for num in range(1, 5)]
     return posList
def collectNegativeListComprehension(lst) :
     negList = [ ele for ele in lst if ele < 0 ]
     return negList

# ----------- METHOD-3 ==  Using lambda functions- In the combination of filter function ------------

def posNumListUsingLambda(lst):
        itObj = filter(lambda ele : ele >= 0 , lst) # it will store only those element who would satisfy the condtion
        posList = list(itObj)
        return posList

def negNumListUsingLambda(lst):
        itObj = filter(lambda ele : ele<0 , lst) 
        negList = list(itObj)
        return negList

myList = [2, 6, -10, -3, 1, -9, 10]
print(f"ORIGINAL LIST: {myList}")
print(f"************************************* METHOD-1 -- Traversal************************************* ")
print(f"Positive Number  LIST: {collectPositive(myList)}")
print(f"Negative Number  LIST: {collectNegative(myList)}")

print(f"************************************* METHOD-2 -- List comprehension ************************************* ")
print(f"Positive Number  LIST: {collectPositiveListComprehension(myList)}")
print(f"Negative Number  LIST: {collectNegativeListComprehension(myList)}")

print(f"************************************* METHOD-3 -- Using lambda functions ************************************* ")
print(f"Positive Number  LIST: {posNumListUsingLambda(myList)}")
print(f"Negative Number  LIST: {negNumListUsingLambda(myList)}")

# I/O 
'''
ORIGINAL LIST: [2, 6, -10, -3, 1, -9, 10]
************************************* METHOD-1 -- Traversal*************************************
Positive Number  LIST: [2, 6, 1, 10]
Negative Number  LIST: [-10, -3, -9]
************************************* METHOD-2 -- List comprehension *************************************
Positive Number  LIST: [2, 6, 1, 10]
Negative Number  LIST: [-10, -3, -9]
************************************* METHOD-3 -- Using lambda functions *************************************
Positive Number  LIST: [2, 6, 1, 10]
Negative Number  LIST: [-10, -3, -9]

'''