#Problem: Remove duplicate element from a list while preserving ORDER.

# Approaches :
'''
1-> By casting into set and then list.
2->Counter function from Colleciton Module : We know about Counter function from Collection module. It count the frequency of each items and return a Counter({}) object that can be easily cast into dictionary and used like dict. And since we got dictonary means we can get all the keys that will be unique means ony one.
'''
#  NOTE: If you have Python 3.7 or later, we can use the built in dict.fromkeys(list) instead. This will also guarantee the order.

from collections import OrderedDict,Counter

def bySet(lst):
    lst[::] = list(set(lst)) # since list is mutable hence no need to return anythng.
    

def byCounterFun(lst):
    uniqVal = dict(Counter(lst)).keys() # but in this approach it not guaranty for order preservance.
    lst[::]= list(uniqVal)


# More specifically, we can use OrderedDict.fromkeys(list) to obtain a dictionary having duplicate elements removed, while still maintaining order. We can then easily convert it into a list using the list() method.
def  byOrderDictClass(lst):
      b = OrderedDict.fromkeys(lst) # it create ordered dict so it gauranty order preservance.
      lst[::] = list(b)
                    
#Multiple APproaches for REF:  https://www.askpython.com/python/remove-duplicate-elements-from-list-python#:~:text=If%20you%20want%20to%20preserve,removed%2C%20while%20still%20maintaining%20order.                    
              
              


myList1 = [5, 55, 10, 4, 55, 5] # [10, 4, 5, 55] -  but in this approach order is not preserve
print(f"ORIGINAL LIST1: {myList1}")
print(f"************************************* METHOD-1 -- Casting into SET ************************************* ")
bySet(myList1)
print("After removing Duplicate elements list1: ", myList1)

print(f"************************************* METHOD-2 -- Counter Class from Collection module ************************************* ")
myList2 = [1, 2, 4, 2, 6, 1]
print(f"ORIGINAL LIST2: {myList2}")
byCounterFun(myList2)
print("After removing Duplicate elements List2: ", myList2)

print(f"************************************* METHOD-3 -- OrderedDict Class  from Collection module ************************************* ")
myList3 = [1, 12, 4, 2, 6, 12, 4]
print(f"ORIGINAL LIST3: {myList3}")
byOrderDictClass(myList3)
print("After removing Duplicate elements List2: ", myList3)


# INPUT/OUTPUT :
'''
Python-List\14_rmvDuplElemFrmLstWhilePreserveOrder.py"
ORIGINAL LIST1: [5, 55, 10, 4, 55, 5]
************************************* METHOD-1 -- Casting into SET *************************************
After removing Duplicate elements list1:  [10, 4, 5, 55]
************************************* METHOD-2 -- Counter Class from Collection module *************************************
ORIGINAL LIST2: [1, 2, 4, 2, 6, 1]
After removing Duplicate elements List2:  [1, 2, 4, 6]
************************************* METHOD-3 -- OrderedDict Class  from Collection module *************************************
ORIGINAL LIST3: [1, 12, 4, 2, 6, 12, 4]
[1, 12, 4, 2, 6]
After removing Duplicate elements List2:  [1, 12, 4, 2, 6]

'''
