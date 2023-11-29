

# Python Program to print duplicates from a list of integers

#INFO:
'''
A duplicate element in a list is the element that has occurred more than once in the list. 
We can print duplicates by following various approaches.

Given a list of integers, we have to print all those integers which have occurred more than once in the list.

Input: [10, 2, 2, 3, 1, 6, -3, -2, 3, 4, 8, 10]
Output: [10, 2, 3]

For printing duplicate integers from a list in Python, we can follow these approaches:

1---> Brute force approach
2---> using count() method
3---> using Counter() functiond with LIST comprehension

'''

from collections import Counter

# m-1 => Brute Force approach:
def traversalBrutForceMethod (lst):# comparing 
    dupList = []
    for currentInd in range(len(lst)) : # extract current element index       
            nextIndex = currentInd + 1 # so that we can compare with the next element 
            for ind in range (nextIndex, len(lst)) : # comparing element with the current extracted elelemt
                if  lst[ind] == lst[currentInd] and  not lst[currentInd] in dupList:# ALSo curent proceeding elelemnt must not already append 
                      dupList.append(lst[currentInd])
    else:
          return dupList

# m-2 => count() method with condition check approach:
def countMethodApproach(lst):
      dupList = []
      for ele in lst :
            timesOccur = lst.count(ele) # it count how many number of time the given element ouccured in the list
            if timesOccur > 1 and ele not in dupList:
                dupList.append(ele)
      else:
            return dupList


# m-3 => count() FUNCTION with LIST COMPREHENSION approach:
def counterFnctionApproach (lst) :
      dupCount = Counter (lst)
      dupCountInDict = dict(dupCount)   
      dupList = [ele for ele in dupCountInDict if dupCountInDict[ele]>1] # since in for loop when we iterate it gives key by default.
                                            #           we are checking if ele (key) value greater one .
      return dupList


myList = [10, 2, 2, 3, 1, 6, -3, -2, 3, 4, 8, 10]

print(f"ORIGINAL LIST: {myList}")
print(f"************************************* METHOD-1 -- Traversal and comparing ************************************* ")
print(f"Duplicate element of above LIST: {traversalBrutForceMethod(myList)}")

print(f"************************************* METHOD-2 --count() method with condition check  ************************************* ")
print(f"Duplicate element of above LIST: {countMethodApproach(myList)}")

print(f"************************************* METHOD-3 --count() FUNCTION with LIST COMPREHENSION  ************************************* ")
print(f"Duplicate element of above LIST: {counterFnctionApproach(myList)}")

'''
ORIGINAL LIST: [10, 2, 2, 3, 1, 6, -3, -2, 3, 4, 8, 10]
************************************* METHOD-1 -- Traversal and comparing *************************************
Duplicate element of above LIST: [10, 2, 3]
'''

# Approach 1: Brute force approach:


'''
Also known as exhaustive search, in this, we will use two for loops which will count the occurrence of each integer 
in the list and display the duplicate elements based on the count of their occurrence.
'''

# Algorithm
            #Follow the algorithm to understand the approach better.


'''
Step 1- Define a function to find duplicates
Step 2- In the function declare a EMPTY list that will store all the duplicate integers
Step 3- Run a loop for each element in the list on range(len(lst)) ==> this will give current index by which we can current elelemtn.
Step 4- For each integer, run another loop that will check if the same integer is repeated.FROM NEXT index start running loop. so that we can next element by next index.
Step 5- Compare cureent elelent and next element AND current is already in the Empty list or not
Step 6- If found the repeated integer will be added to another list using append(). if Satisfy TRUE  append it.
Step 7- Return the list which stores repeated integers
'''

# Approach 2: Counter() function
'''
Counter() is a built-in function that returns a dictionary of all the elements and their occurrences in a list. A dictionary has keys and values corresponding to it, the elements in the list and their occurrences are returned in a similar way.

After getting occurrences of each integer, we will check which integers occurred more than once and then store them in another list.
'''
# Algorithm
            # Follow the algorithm to understand the approach better.
'''
Step 1- Import Counter function : Counter() function in your program, import it from the collections module. 
Step 2- Take list with integer values
Step 3- Use Counter() to calculate occurrences of all the numbers in the list : COUNTER({elemnt : occurence,.......}). that y make list after applying counter()
Step 4- Declare another list
Step 5- Use a list comprehension to store integers with occurrence more than 1 in the list
Step 6- Return the Duplicate list

EX:
li=[1, 3, 2, 6, 2, 3, 5, 6, 4, 5]
d = Counter(li)
print d   ==> OUTPUT:  Counter({3: 2, 2: 2, 6: 2, 5: 2, 1: 1, 4: 1})
so its similar to dict but not exactly BUT we cast it and that will become more esay to understand. like below
dct = dict(d)
print d ==> OUTPUT:  {3: 2, 2: 2, 6: 2, 5: 2, 1: 1, 4: 1}
'''