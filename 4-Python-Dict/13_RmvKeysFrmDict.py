# Python Program to remove a key from dictionary

# we will learn to write a program to remove a key from a dictionary in Python. Keys in a dictionary are unique and should be of an immutable data type such as strings, numbers, or tuples. For a given dictionary with values, the task is to delete a key-value pair from the dictionary.

# Look at the example to understand the input-output format.
'''
my_dict: {'x': 20, 'y': 10, 'z': 90 }  after deleting 'x'
Output: { 'y': 10, 'z': 90 }
'''
# To solve this problem in Python, we can use the following approaches:
'''
---> Using del keyword : We'll not be using this - reason is mention below
---> Using pop()
---> Using items() and dictionary comprehension : In this approach we have to create new dict(since use of dict comprehension)& in that desired rmved key will not be there. 
'''

# Method dct.pop():  By using pop Dict method : it removed value and key provide key and return the value of deleted key 
# pros: This approach is better than using del because pop() will not give any exception if the key is not present in the dictionary.
def usingPop(dct , key) :
        rmvVal= dct.pop(key)
        print(f"Removed element of key {key} : {rmvVal}")
        return dct

# Method dct.items() : and creating new dict.
def usingItems(dct, key):
            newDict  = {dctKey : value for dctKey, value in dct.items() if dctKey != key}      
            return newDict



my_dict = {'x': 20, 'y': 10, 'z': 90 }
key1 = 'x'
print(f"Original Dict : {my_dict}" )
print("*********************   WAY - 1 : By using dct.pop() Dict method ***********************")
print(f"Remaining Dict after removing value and key ({key1}) : {usingPop(my_dict , key1)}")

key2 = 'z'
print(f"Original Dict : {my_dict}" )
print("*********************   WAY - 2 : By using dct.items() Dict method with dict comprehension ***********************")
print(f"Remaining Dict after removing value and key ({key2}) : {usingItems(my_dict , key2)}")



# In this approach, the del keyword is use to delete the key along with value that is present in the dictionary.
''' 
The only drawback of this method is that if the key is not present in the dictionary the del keyword will 
raise an exception which has to be handled separately.
'''

#  drawback of dict comprenhension ans itmems()
'''
The items() method is a method of the dictionary class. It returns both keys and values in a dictionary. The drawback of this method is that
it creates a copy of the dictionary without the key that has to be deleted.
Dictionary comprehension is used to make a copy of the original dictionary which will not have the key-value pair that has to be deleted.
'''


#  I/O:
'''
Original Dict : {'x': 20, 'y': 10, 'z': 90}
*********************   WAY - 1 : By using dct.pop() Dict method ***********************
Removed element of key x : 20
Remaining Dict after removing value and key (x) : {'y': 10, 'z': 90}
Original Dict : {'y': 10, 'z': 90}
*********************   WAY - 2 : By using dct.items() Dict method with dict comprehension ***********************
Remaining Dict after removing value and key (z) : {'y': 10}

'''