# Prog: Python dictionary with keys having multiple inputs

# We will learn to create a dictionary with keys having multiple inputs in Python. We have to create a dictionary, in which there will be one key for multiple inputs.

# Take a look at the sample input-output of the program.In this case will have to use both list index concpt and dict.
'''
Input: x= 2 y= 1 z=9 , p=3, p=5, r=2
Output: {'x+y+z' : [12, 10]}

Input: {''words with d" : ['dog', 'dark', 'dance'] , "words with a": ['apple', 'act', 'ace']}
Output:{''words with d" : ['dog', 'dark', 'dance', 'den'] , "words with a": ['apple', 'act', 'ace','all']}
'''
# To solve this problem, we will first create an empty dictionary and insert multiple values in it. 
# We will see two examples of when we have to create a dictionary with keys having multiple inputs.

# Example 1: linear equation as key
'''
For this let us consider an example where we have a linear equation of three vari\ables x, y, and z. 
We have to store the values given by the equation for different values of x,y, and z given as input.
'''
def fun1 (dct, key) :
    x, y, z, p, q, r = 2, 1, 9, 3, 5, 2 #input 
    t1 = x+y+z # equation satisfying
    t2 = p+q+r
    dct[key] = [t1, t2]
    return dct

def fun2 (dct, key):
    # Inserting first inputs in dictionary
    a,b,c= 5, 3, 10
    # Insert second inputs in dictionary
    p,q,r= 12, 6, 9
    dct[key] = [a-b+c, p-q+r]
    return dct


# In this example, we will have to create a dictionary where the state name is the key and the different cities in the state are its values.
def add_values_in_dict(dct, key, listOfCities) :
    dct[key].extend(listOfCities) # dct[key] is list hence we need to appned iterable means multiple values at once then we use lst.extend(itr) instead of lst.append().
    return dct


myDict1 = {}
key1 = 'x+y+z' # equation1
print(f"Original Dict : {myDict1}" )
print("*********************   WAY : By exampl-1 method ***********************")
print(f"after inserting  : {fun1(myDict1, key1)}")

myDict2 = {}
key2 = 'x-y+z' # equation2
print(f"Original Dict : {myDict2}" )
print("*********************   WAY : By exampl-2 method ***********************")
print(f"after inserting  : {fun2(myDict2, key2)}")

# dictionary containing states and its cities
places = {("Maharashtra"):["Mumbai","Pune","Nagpur"],
          ("Madhya Pradesh"):["Delhi","Bhopal","Indore"]}

key = "Madhya Pradesh"
val =  ["Ujjain", "Sagar"] # we need to insert in the existing list of cities in this key

print("*********************   WAY : By exampl-3 adding multiple val inexisting method ***********************")
print(f"Original Dict : {places}" )
print(f"after inserting in the above : {add_values_in_dict(places, key, val)}")


# I/O:
'''
Original Dict : {}
*********************   WAY : By exampl-1 method ***********************
after inserting  : {'x+y+z': [12, 10]}
Original Dict : {}
*********************   WAY : By exampl-2 method ***********************
after inserting  : {'x-y+z': [12, 15]}
*********************   WAY : By exampl-3 adding multiple val inexisting method ***********************
Original Dict : {'Maharashtra': ['Mumbai', 'Pune', 'Nagpur'], 'Madhya Pradesh': ['Delhi', 'Bhopal', 'Indore']}
after inserting in the above : {'Maharashtra': ['Mumbai', 'Pune', 'Nagpur'], 'Madhya Pradesh': ['Delhi', 'Bhopal', 'Indore', 'Ujjain', 'Sagar']}

'''



