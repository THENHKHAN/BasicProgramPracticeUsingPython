# Python Program to Split the array and add the first part to the end
''''
we will learn how to split an array at a specified position and add the first part to the end. The user will specify the position from where the array has to be split and our program should move the first part of the array to the end of the array.
Take look at the explanation given below,
Suppose there is an array[] with the elements [2, 3, 5, 12, 14, 27, 9] as follows
the user gives an input of p=3 which will specify the position from where the array has to be split(index = position-1 ==> or how many element needs to rotate of shift),
1st part : [2, 3, 5]
2nd part : [12, 14, 27, 9] and
The resultant array should be,
[12, 14, 27, 9, 2, 3, 5]

'''

# Here we used slicing : Which is good for quick solution and if requirment is not specifically said to slipt ad merger in the same list. Since here we'll create another and return new
def SplitArrayUsingSlicing(arr, position):
    # splitting through slicing
    spl1 = arr[:position]
    spl2 = arr[position:len(arr)]
    newMergedArray = [*spl2, *spl1]
    return newMergedArray

# Here we'll make chnages in the same array: More likely to be accepted  :Quick
def SplitArrayAndMadeChnageInExistingArr(arr, position):
    spl1 = arr[:position]
    spl2 = arr[position:len(arr)]
    arr[:] = [*spl2, *spl1]
    # return arr

#  Here we'll make chnages in the same array: More likely to be accepted as well   
def SplitArrayUsingLoop(arr, position):
	for i in range(0, position):
		#  Rotate the array by 1
		x = arr[0]
		for j in range(0, len(arr)-1):
			arr[j] = arr[j + 1]
		
		arr[len(arr)-1] = x
             

# arr = [0,1,2,3,4,5,6,7] #[15, 40, 15, 16, 50, 36]
arr = [2, 3, 5, 12, 14, 27, 9]
position = 3 # that's mean we need to split from this position(or from index = position-1 === 2-1 => 1) ---> part-1 : [0,1]  , part-2 : [2,3,4,5,6,7]
print(f"My Original Array : {arr}" )
print("********************* After splitting and adding 1st to the end: Using SLICING ***********************")
print(f" Resultant Array : {SplitArrayUsingSlicing(arr, position)}")

print("*********************   WAY - 2 : By Using SLICING:InExisting list  ***********************")
SplitArrayAndMadeChnageInExistingArr(arr,position)
print(f"  Resultant Array: {arr}")

print("*********************   WAY - 3 : By Using loop : rotaion elemtn  ***********************")
SplitArrayUsingLoop(arr,position)
print(f"  Resultant Array: {arr}")

# I/O:
'''
My Original Array : [2, 3, 5, 12, 14, 27, 9]
********************* After splitting and adding 1st to the end: Using SLICING ***********************
 Resultant Array : [12, 14, 27, 9, 2, 3, 5]
*********************   WAY - 2 : By Using SLICING:InExisting list  ***********************
  Resultant Array: [12, 14, 27, 9, 2, 3, 5]
*********************   WAY - 3 : By Using loop : rotaion elemtn  ***********************
  Resultant Array: [9, 2, 3, 5, 12, 14, 27]
'''

# Algorithm:
''' for 3rd approach:

Follow the algorithm to understand the detailed working of the program.

Step 1- Define a function SplitArray() which will split the array and add the first part to the end
Step 2- Run a loop from the starting index to the index where the array has to be split
Step 3- Inside the loop, store the first element of the array in a variable x
Step 4- Run a loop inside the first loop from starting to the ending index and shift the elements to the left side
Step 5- When all the elements are shifted keep the first element at the last index
Step 6- Repeat the process for all elements which are in the first part of the array
Step 7- Define another function to print the array
Step 8- Specify the array and the position from where the array has to split
Step 9- Call the function and pass the array and the position
Step 10- Print the resultant array

Complexity Analysis
Time complexity: O(n*k) where n is the size of the array and k is the number of times we have traversed the array. The time complexity is O(nK) as the array is traversed k times.
Space complexity: O(1) as no new memory is created.

OR:
Brute Force Approach
To split the array and add the first part to the end, we can rotate the elements of the array one by one.

Pseudocode
Step 1: Initialize the array and the position where we want to split the array.

Step 2: Create a variable to store the element at the 0th position.

Step 3: Replacing each element ‘i’ of the array with the element at the ‘i+1’ position.

Step 4: Replacing the last element of the array with the element stored in the variable created in step 2.
'''

#  IMP : ref:
'''
def split_and_add(arr, n):
	return [arr[(i + n) % len(arr)] for i in range(len(arr))]


arr = [12, 10, 5, 6, 52, 36]
n = 2

result = split_and_add(arr, n)

print(*result)
Time complexity: O(n) : where n is length of the input array. This is because we use a list comprehension to create a new list, and this operation takes O(n) time. The modulo operation % takes constant time, so it does not contribute to the overall time complexity.
Auxiliary space: O(n) : we create a new list of the same length as the input array. This list is used to store the results of the computation, so it takes O(n) space in memory.


ANOTHER: Using Deque
'''