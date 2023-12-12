# Python program to find the sum of all items in a dictionary

#  We will learn to find the sum of all items in a dictionary in Python. Dictionaries hold values in a key-value pair format, where each value has its own unique key. For a given dictionary with values, we have to find the sum of all items in the dictionary and print the result.

# Look at the example to understand the input-output format.
'''
Input: {'k1 ': 120, 'k2' : 20, 'k3' : 300}
Output: 440
Input: {'a' : 200, 'b' : 360, 'c' : 550}
Output: 1110
'''
# To solve this problem in Python, we can use the following approaches:
'''
--> By using sum() and values()
--> By using the iterative method
'''
# method-1 : Easy : 1st get all values as list and  then use sum()- pre-defined python funciton
def bySumValuesFun(dct):
        listOfVal =list( dct.values())
        return sum(listOfVal)   # we could skip the above by using this : return sum( dct.values())
 
#  method-2
def byIterativeApproach (dct) :
        sum = 0
        for val in dct.values():
                sum += val        
        return sum


my_dict = {'k1 ': 120, 'k2' : 20, 'k3' : 300}
print(f"Original Dict : {my_dict}" )
print("*********************   WAY - 1 : By sum() and values() ***********************")
print(f"Sum of Values of  Dict : {bySumValuesFun(my_dict)}")


print("*********************   WAY - 2 : By Iterative Approach ***********************")
print(f"Sorted Dict : {byIterativeApproach(my_dict)}")


