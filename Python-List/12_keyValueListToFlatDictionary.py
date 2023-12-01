
# Python program to Convert key-values list to flat dictionary- using ZIP() and dict() built-in function

# INFO
'''
We will learn how to write a program that will convert a key-value list to a flat dictionary using the Python programing language. 
For a given dictionary with pairs of key-value as a list, we have to convert this list to a flat dictionary. A dictionary can be 
flattened by pairing the same index elements together.

Let us look at the sample input-output of the program.

Input: { "num": [1, 2, 3], "name": ['Monica', 'Joey', 'Jane' ] }
Output: {1: 'Monica', 2: 'Joey', 3: 'Jane'}
**--> we'll extract list through keys and then with the help of zip we made tuple one list work as a key and other as a value. and then cast it int o dict.
To solve this problem in Python, we can use a combination of methods of the dictionary class- zip() and dict().

---> The zip() method is a built-in function that accepts iterables as parameters and returns a tuple of the elements from each iterable
---> The dict() method is a built-in function used to create a dictionary in Python.

THIS IS HOW WE CAN MAKE LIST FROM TUPLE :
a = (1,2)
b = (55,100)
d = zip(a,b)
print(d) # <zip object at 0x00000213CF84BE00>
print(dict(d)) # {1: 55, 2: 100}
'''
def makeDictFromZip(): # just to know how to make dict from zip.zip()takes two iterables as parameters and returns a tuple of the elements from each iterable
    a = (1,2) # this be list as well 
    b = (55,100)
    d = zip(a,b) # 1st iterable work as a key for dict and 2nd as a value corresponding to each element
    print(d)
    print(dict(d)) 


def getDict (dct) :
    for key, value in dct.items():
        print(f"{key} : {value}")

    l1 = dct["num"]
    l2 = dct["name"]
    zipObj = zip(l1, l2) # it will store like this ( (1, 'Monica'),( 2, 'Joey'), (3, 'Jane') ) 
    flattenDict = dict( zipObj) # converting tupple to dict

    return flattenDict

myDict = { "num": [1, 2, 3], "name": ['Monica', 'Joey', 'Jane' ] }
print(f"ORIGINAL Dict: {myDict}")
print(f"************************************* after making dict from existing above dict ************************************* ")
print(f"Flatten DICT: {getDict(myDict)}") # Flatten DICT: {1: 'Monica', 2: 'Joey', 3: 'Jane'}


# Algorithm
# Follow the algorithm to understand the approach better.
'''
Step 1- Initialise dictionary with key and value as list of element.
Step 2- Print original dictionary
Step 3- Declare another dictionary that will store the elements grouped together (This will be our resultant Dictionary)
Step 4- Use zip() to get the elements in the dictionary in the form of a tuple
Step 5- Use dict() to convert the tuple to a dictionary
Step 6- Print the new dictionary as the result
'''