# we will learn to write a program that will sort a dictionary in Python. Sometimes, there may be a task in which we will have to sort the dictionary. We can sort a dictionary based on the key or the value. We will be discussing how to sort the dictionary based on the values in this tutorial. We can perform this task easily in Python using built-in methods.

# Look at the example to understand the input-output format.
'''
Input: {'A': 3, 'B': 1, 'C': 10, 'D': 2}
Output: {'B': 1, 'D': 2, 'A': 3, 'C': 10}
'''
# To solve this problem in Python, we can use the following approaches:
'''
--> Sort the values using sorted() and with key- dict.get 
--> Sort the values alphabetically using lambda functions
--> Sort the keys alphabetically using for loop and sorted() function
'''


# method-1 : using sorted() function and paramter key. Here key is the funciton keyword - dict.get
def bySortedAndGet(dct):                            # if we set reverse = True then it will sort in descending order
    sortedKeybasedOnthereValues = sorted(dct, key=dct.get , reverse=False)  # dct.get we'll get values based on each key and sorted funciton then sorted function sort the values and return list of keys based on soretd  values
                                    # key is like a function
    print("Sorted Keys based on values: ", sortedKeybasedOnthereValues) # ['Kane', 'Tina', 'Tom', 'Divya', 'Akbar'] 
    sortedDict = {}
    for key in sortedKeybasedOnthereValues :
        sortedDict [key] = dct[key]
    
    return sortedDict
# method-3 :  By using a for loop along with sorted() function in Python, we can sort the dictionary by value.

# method-2 :
def bySortedAndLambda(dct):
    sorted_tuples  = sorted (dct.items(), key = lambda x : x[1]) # [('Kane', 43), ('Tina', 54), ('Tom', 67), ('Divya', 73), ('Akbar', 87)]. Here we can see values are sorted
    # we have to get those values of the dictionary so we can sort the dictionary by values. That’s why you can see 1 in the lambda function.
    # 1 represents the indexes of the values. The keys are 0. Remember that a programmer starts counting from 0, not 1.
    print("Sorted Keys based on values: ", sorted_tuples ) # [('Kane', 43), ('Tina', 54), ('Tom', 67), ('Divya', 73), ('Akbar', 87)]
    # return dict(sorted_tuples) OR 
    return {key: value for key, value in sorted_tuples} # just like list comprehension so its a dictionry comprehnsion


def bySortedAndForLoop(dct):
    sorted_val = sorted(dct.values()) # it retunrs list of values in sorted order 
    print("Sorted values : ", sorted_val ) # [43, 54, 67, 73, 87]

    #  now we'll make an empty dict and insert key value but before inserting we'll check  i.e traverse the dicitonary to which values abd key
    sortedDict ={}
    for val in sorted_val:
            for key in dct.keys():
                if dct[key] == val :
                     sortedDict[key] = dct[key]
    
    return sortedDict
                 


# my_dict= {1: 13, 2: 7, 3: 0, 4: 10 }
my_dict= {"Tom":67, "Tina": 54, "Akbar": 87, "Kane": 43, "Divya":73} 
# my_dict = { 'num6': 6, 'num3': 3, 'num2': 2, 'num4': 4, 'num1': 1, 'num5': 5}

print(f"Original Dict : {my_dict}" )
print("*********************   WAY - 1 : By Sorted()fun and get attr ***********************")
print(f"Sorted Dict : {bySortedAndGet(my_dict)}")

print("*********************   WAY - 2 : By sorted and dct.items() and lambda ***********************")
print(f"Sorted Dict : {bySortedAndLambda(my_dict)}")


print("*********************   WAY -  : By for Loop along with sorted() fun ***********************")
print(f"Sorted Dict : {bySortedAndForLoop(my_dict)}")




