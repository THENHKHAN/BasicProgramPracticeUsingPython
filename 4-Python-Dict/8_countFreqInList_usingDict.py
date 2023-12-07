# Counting the frequencies in a list using dictionary in Python
'''
We will learn to write a program in Python that will count the frequency of elements in a list using a dictionary. For a given list with multiple elements,
we have to count the occurrence of each element in the list and display it as output. This can be done by creating a dictionary and using some built-in methods
which will be discussed below.

'''
# Look at the input-output format to understand better.
'''
Input: ['a', 'a', 'a', 'b','b']
Output: {'a': 3, 'b': 2}

To solve this problem we can follow these approaches-

0-->using Counter Class constructor => great for such things- its a subclass of dict. It return Counter obj and we can type cast into Dict then we can  use like we use Dict.
1-->by iterating over the list and counting frequency
2-->using list.count() method
3-->using dict.get() method

'''
from collections import Counter


# method-0 - my Fvr
def CountFreq(lst):
    countObj = Counter(lst)
    return dict(countObj)


# method-3 : dict.get() method - kind of iterator
def CountFreqByDictGet(lst):
    storeFreq = {}
    for ele in lst:
        if ele in storeFreq:
            storeFreq[ele] = storeFreq.get(ele, 0) + 1
        else:
            storeFreq[ele] = 1

    return storeFreq


# method-2 :
def CountFreqBycountMethod(lst):  # lst.count(ele) : count return frequency of provided ele as argument from the list.
    dct = {}
    for ele in lst:
        if ele not in dct:
            dct[ele] = lst.count(ele)
        else:
            pass
    return dct

# method-1 : iterating and counting each ele
def CountFreqByIter(lst):
    storeFreq = {}
    for ele in lst:
        if ele in storeFreq:
            storeFreq[ele] = storeFreq[ele] + 1
        else:
            storeFreq[ele] = 1

    return storeFreq


# myList = ['a', 'a', 'a', 'b', 'b']
myList = [1, 1, 3, 2, 6, 5, 3, 1, 3, 3, 1, 4, 6, 4, 4, 2, 2, 2, 2]
print("*********************   WAY - 1 : Counter() Constructor  ***********************")
print(f"Frequency of each Char : {CountFreq(myList)}")

print("*********************   WAY - 2 : Iterating and counting each ele  ***********************")
print(f"Frequency of each Char : {CountFreqByIter(myList)}")

print("*********************   WAY - 3: lst.count() method-  ***********************")
print(f"Frequency of each Char : {CountFreqBycountMethod(myList)}")

print("*********************   WAY - 4: dict.get() method-  ***********************")
print(f"Frequency of each Char : {CountFreqByDictGet(myList)}")

# Approach of iterating :
'''
Step 1- Define a function that will count the frequency of elements in the list
Step 2- Create an empty dictionary
Step 3- Run a loop to traverse the list items
Step 4- To count the frequency, check if the element exists in the dictionary
Step 5- If yes, then increase the value present at the element key by 1,
Step 6- else add that element as key and set its value as 1
Step 7- Print the dictionary as the result
'''

# I/O:
'''
*********************   WAY - 1 : Counter() Constructor  ***********************
Frequency of each Char : {1: 4, 3: 4, 2: 5, 6: 2, 5: 1, 4: 3}
*********************   WAY - 2 : Iterating and counting each ele  ***********************
Frequency of each Char : {1: 4, 3: 4, 2: 5, 6: 2, 5: 1, 4: 3}
*********************   WAY - 3: lst.count() method-  ***********************
Frequency of each Char : {1: 4, 3: 4, 2: 5, 6: 2, 5: 1, 4: 3}
*********************   WAY - 4: dict.get() method-  ***********************
Frequency of each Char : {1: 4, 3: 4, 2: 5, 6: 2, 5: 1, 4: 3}
'''
