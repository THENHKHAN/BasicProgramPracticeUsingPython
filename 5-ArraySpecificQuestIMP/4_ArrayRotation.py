# Python Program for Array Rotation
'''
we will learn how to write a function for Array Rotation. The user will give an input d by which the elements of the array will be rotated.

Python arrays are data structures that store homogenous data. Arrays stores objects of the same datatype. Arrays are mutable, 
meaning that the data in an array can be changed and iterative, meaning each element in an array can be accessed one by one.
'''
# EXAMPLE:
'''
Input-[1, 2, 3, 4, 5, 6] , position: 2  => means two element nee to rotate ==> means 0 to position-1 ===indx  we need to rotate 
Output-Rotated array is [3, 4, 5, 6, 1, 2]

For executing this task we will follow these approaches:

1----> Using a temporary array that will store the shifted elements
2-----> Slicing the array
'''

# using temp array
def usingTempArray(lst, position) :

    tempArr = []
    for ind in range(position, len(lst) ):
        tempArr.append(lst[ind])
    print(f"Temp Array : {tempArr}")

    for ind in range(0, position):
        tempArr.append(lst[ind])
    
    lst = tempArr.copy() # The copy() method returns a copy of the specified list. Returns: Returns a shallow copy of a list.
    # Note: A shallow copy means any modification in the new list won’t be reflected in the original list
    return lst # since above is a shallow copy so lst work as new variable and by this the original list not be modified


#  Slicing the array

def usingSlicing(lst, position) :
    split1 = lst[0:position]
    split2 = lst[position: ]
    lst[ : : ] = split2+split1 # chnage order while again reassing. OR unpacking - [ *split2, *split1]
    return lst


arr = [1, 2, 3, 4, 5, 6, 7] #, d = 2, n =7
print("******************* METHOD - 1 Temp array stored  **********************************")
print("Original Array :  " , arr)
position = 2
print(f" After rotaion of {position} Element Resultant Array: {usingTempArray(arr,position)}")
print("Original Array :  " , arr)

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
# thislist = [1, 2, 3, 4, 5, 6, 7]
print("******************* METHOD - 2 Slicing way   **********************************")
print("Original Array :  " , thislist)
position = 2
print(f" After rotaion of {position} Element Resultant Array: {usingSlicing(thislist,position)}")
print("Original Array Also chnaged:  " , thislist)


#  I/O:
'''
******************* METHOD - 1 Temp array stored  **********************************
Original Array :   [1, 2, 3, 4, 5, 6, 7]
Temp Array : [3, 4, 5, 6, 7]
 After rotaion of 2 Element Resultant Array: [3, 4, 5, 6, 7, 1, 2]
Original Array :   [1, 2, 3, 4, 5, 6, 7]
******************* METHOD - 2 Slicing way   **********************************
Original Array :   ['apple', 'banana', 'cherry', 'apple', 'cherry']
 After rotaion of 2 Element Resultant Array: ['cherry', 'apple', 'cherry', 'apple', 'banana']
Original Array :   ['cherry', 'apple', 'cherry', 'apple', 'banana']
'''


#  Approach 1: By Using a temporary array
# In this approach, we will declare a temporary array that will store the array elements in a shifted order.
'''
Input arr[] = [1, 2, 3, 4, 5, 6, 7], d = 2, n =7

1) Store all the elements in the index range d to n in a temp array
   temp[] = [3, 4, 5, 6, 7]
2) Add all the elements in the index range 0 to d in the temp array
   arr[] = [3, 4, 5, 6, 7, 1, 2]
3) Copy the temp array to arr[]
   arr[] = [3, 4, 5, 6, 7, 1, 2]
'''
# Algorithm
'''
Step 1- Define a function to rotate the array
Step 2- Declare a temporary variable
Step 3- Use len() to calculate the length of the array and store it in a variable
Step 4- Run a loop from d to n and store the elements at each index in the temp array
Step 5- Run another loop to add the rest of the elements to the temporary array
Step 6- Copy temp array to original array
Step 7- Return array

'''

# Approach 2: Slicing
'''
In this approach, we will use the concept of slicing. Since the array is a type of list with elements of the same data type 
we can use the concept of list slicing here. Through slicing, we can access any part of the array.
'''
# Algorithm
'''
Step 1- Define a function to rotate elements in the array list
Step 2- Define the length of an array using len()
Step 3- Use splicing operator ( : ) to store the elements from d to n and 0 to d
Step 4- Use ( + ) to concatenate both arrays
Step 5- Return array
'''