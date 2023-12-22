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

def SplitArray(arr):
    pass


arr = [0,1,2,3,4,5,6,7] #[15, 40, 15, 16, 50, 36]
position = 2 # that's mean we need to split from this position(or from index = position-1 === 2-1 => 1) ---> part-1 : [0,1]  , part-2 : [2,3,4,5,6,7]
print(f"My Original Array : {arr}" )
print("********************* After splitting and adding 1st to the end ***********************")
print(f" Resultant Array : {SplitArray(arr)}")



# Algorithm:
'''
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
'''