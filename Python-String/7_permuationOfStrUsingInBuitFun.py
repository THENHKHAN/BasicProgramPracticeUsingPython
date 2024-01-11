# Python Program for Permutation of a given string. Here we'll be using python inbuilt funciton permuation(iter) from itertools module
#  NOTE: we'll do it later by backtracking etc....

'''
In this tutorial, you will learn to get different permutations of a given string using an inbuilt function in Python. A permutation is simply a re-arrangement of the elements in different possible orders. Strings in Python are a sequence of characters wrapped in single, double or triple quotes. Strings are made up of characters. Permutation of a string will be the set of all possible ways in which the order of the characters of the string can be changed.
Let us look at the sample input and output of the program.

Input: "pqr"
Output: pqr prq qpr qrp rqp rpq

Input: "AB "
Output: AB BA

Note : by default we'll choose the same number of character as the string is. That' why npr here r = n : n!/(n-r)! will be possible permuation. 
'''

from itertools import permutations

def allPermutations(givenStr) :
        lst = []
        p = permutations(givenStr) # will return permuation object so we have to cast in some iterator like list or tuple
        listOfTupleOfChar = list(p) # [('p', 'q', 'r'), ('p', 'r', 'q'), ('q', 'p', 'r'), ('q', 'r', 'p'), ('r', 'p', 'q'), ('r', 'q', 'p')]
        for perm in listOfTupleOfChar: # perm will be tuple like this  : ('p', 'q', 'r')  , silimilary other
                permStr = ''.join(perm) # join is a funxtion that takes a iterator and join them and make into a single string : ('p', 'q', 'r') ==> pqr
                lst.append(permStr)
        print("Total possible number of permuation will be : ", len(lst))
        print(f"all possible Permutations of a string - {givenStr} : {lst}") # ['pqr', 'prq', 'qpr', 'qrp', 'rpq', 'rqp']



InputStr = "pqr"
print("My Input String:  " , InputStr)
allPermutations(InputStr)





#  APPROACH:

'''
To solve this problem we will be using the built-in function permutations() from the itertools module. Python's itertools is a module that provides various 
functions that work on iterators to produce complex iterators. . The permutations() method takes a list, dictionary, tuple, or other iterators as a parameter 
and returns the permutations of that list.

We can use this method to return a list of all possible permutations of a string. To get the result in string format we will use the join() method. 
It will join the list elements together to form a string.

'''