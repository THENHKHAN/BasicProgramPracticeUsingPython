# Python Program to Extract Unique values from a dictionary

# we will learn to extract unique values from a dictionary in Python. Dictionary in Python is a data type for an ordered collection of data values. Dictionaries hold a key-value pair where each value is linked with a unique key.
'''
Look at the example to understand the input-output format.

Input: {
'A' : [1, 3, 5, 4],
'B' : [4, 6, 8, 10],
'C' : [6, 12, 4 ,8],
'D' : [5, 7, 2]
}
Output: [1, 2, 3, 4, 5, 6, 7, 8, 10, 12]
'''
# To solve this problem in Python, we can use the following approaches:
'''
--> Using list() , values() and set()-(for uniqueValue) and two for loop
--> Using sorted(), values() and list comprehension OR set comprehension
--> Using sorted(), values() and chain()

'''
from itertools import chain

#Method-1
def byTwoForLoop(lstOflist): # simple method whihc i thought from scratch
    emptLst = []
    for lst in lstOflist :
        for ele in lst :
            emptLst.append(ele)
    setOfUniqValues = set(emptLst)
    listOfUniqvalues = list(setOfUniqValues)
    return listOfUniqvalues

# method-2
def byListCompre(lstOflist): # learnt how use list comprehension as set comprehension
        listOfUniqValues = {ele for lst in lstOflist for ele in lst } # i have used {} to make it unique :  [sorted({ele for lst in lstOflist for ele in lst}) ] we can sort by this
        return list(listOfUniqValues)


# method-3: Using sorted(), values() and chain()
def byChainFunc(dct) :
    #  val = chain(*dict.values)  # print (val) : <itertools.chain object at 0x000001D3FB81BE50>   
    val = set(chain(*dct.values()))  
    return list(val)

dct = {
            'A' : [1, 3, 5, 4],
            'B' : [4, 6, 8, 10],
            'C' : [6, 12, 4 ,8],
            'D' : [5, 7, 2]

        }
lstOfValues = list(dct.values()) # it return list of values of dict
print(f"my Dictinoary : {dct}")
print("*********************   WAY - 1 : By Two loop set() ***********************")
print(f"List of Unique Values of Above dictionary Dict : {byTwoForLoop(lstOfValues)}")

print("*********************   WAY - 2 : By  sorted(), values() and list comprehension ***********************")
print(f"List of Unique Values: {byListCompre(lstOfValues)}")# learnt how to use double for loop in ;ist comprehension

print("*********************   WAY - 3 : By  chain()funciton values() and list comprehension ***********************")
print(f"List of Unique Values : {byChainFunc(dct)}")# learnt how to use double for loop in ;ist comprehension


# VERY IMPP ABOUT UNPACKING WITH DICT
'''
dct = {'A': [1, 3, 5, 4], 'B': [4, 6, 8, 10], 'C': [6, 12, 4, 8], 'D': [5, 7, 2]}
print(*dct.values()) #  [1, 3, 5, 4] [4, 6, 8, 10] [6, 12, 4, 8] [5, 7, 2]            HOW?????????????????
EXPLAIN:
Here, dct.values() returns a view of all the values in the dictionary dct. The * (asterisk) is the unpacking operator, which is used to unpack the values from the 
view and pass them as separate arguments to the print function.

So, when you execute print(*dct.values()), it's equivalent to calling print with each list of values as a separate argument:

print([1, 3, 5, 4], [4, 6, 8, 10], [6, 12, 4, 8], [5, 7, 2])
Result : [1, 3, 5, 4] [4, 6, 8, 10] [6, 12, 4, 8] [5, 7, 2]

'''

# ABOUT CHAIN() fubnction : it flattern the list - 
'''
from itertools import chain
dict1 = {'A': [1, 3, 5, 4], 'B': [4, 6, 8, 10], 'C': [6, 12, 4, 8], 'D': [5, 7, 2]}
resultObj =(chain(*dict1.values())) # we can set dunciotn to get the uni and then cast in list
print(list(result_set)) # [1, 3, 5, 4, 4, 6, 8, 10, 6, 12, 4, 8, 5, 7, 2]

EXPLAIN:
The code you provided seems to be using the chain function from the itertools module to flatten a list of lists that are the values of a dictionary (dict1). Additionally, 
it looks like the intention is to convert the flattened result into a set.

Here's what each part does:

dict1.values(): Returns a view of the values in the dictionary dict1. In your case, this is a view of lists.
chain(*dict1.values()): Uses the chain function to flatten the list of lists into a single iterable. The * (unpacking operator) is used to pass each list from dict1.values() as a separate argument to chain.
set(chain(*dict1.values())): Converts the flattened iterable into a set, removing any duplicate elements.
The resulting result_set will contain the unique elements from all the lists in the values of the dictionary. If you print result_set, you will see the output:


EX: 
from itertools import chain

dict1 =[  [1, 3, 5, 4], [4, 6, 8, 10], [6, 12, 4, 8], [5, 7, 2]]
result_set =list(chain(*dict1))
print(result_set)
[1, 3, 5, 4, 4, 6, 8, 10, 6, 12, 4, 8, 5, 7, 2]


'''