# Python program to Merging two Dictionaries
'''
we will learn to write a program to merge two dictionaries in Python. For two given dictionaries, we have to merge them and **return a single dictionary** that will have the values of both 
the dictionaries. Merging simply means that we are joining the two ditionaries together.
'''

# Let us look at the sample input and output to understand better.
'''
Input:

d1= { 'A': 1, 'B': 2 }
d2= { 'x': 3, 'y': 4 }
Output: { 'A': 1, 'B': 2, 'x': 3, 'y': 4 }
'''
# To execute this task in Python, we can follow these approaches:
'''
---> using ** (double star) operator : unpacking
---> using update() method
'''

# method-1 By unpacking into a new dict :  using **(double star) operator
def mergeByUnpacking(dct1, dct2): 
    merge_dct = {**dct1, **dct2} # we have used the ** operator to pass all the key-value pairs of both the dictionaries one by one in the new dictionary. This will merge the dictionary, and we can return the result.
    return merge_dct


# method-2: using update() method of dictionary: The update() method of the dictionary class inserts the values of a dictionary to another dictionary along with the respective keys. 
# ABOUT RETURN : This method ** does not create a new dictionary but only adds elements to the existing dictionary**.
def mergeByUpdateMethod(dct1, dct2):# This method ** does not create a new dictionary but only adds elements to the existing dictionary**.
    dct1.update(dct2) # 2nd will merged in the 1st
    # dont have to return anything bcz it upadte in the existing dictionary : But 

dic1= {'x': 3, 'y' : 8, 'z': 5 }
dic2= {1: 8, 'x': 4, 2: 6}
print("*********************   WAY - 1 : By ** or unpacking ***********************")
print(f"Merged Dict : {mergeByUnpacking(dic1, dic2)}")

print("*********************   WAY - 2 : By d1.update methd(d2) ***********************")
mergeByUpdateMethod(dic1, dic2)
print(dic1)
