
# Prog : Add 2D matrix :
import numpy as np

def printMatrices(m1, m2):
    print("******* MATIRIX - 1 *********")
    for row in m1:
        for col in row:
            print (f"{col} " , end=" ")
        print()
   
    print("******* MATIRIX - 2 *********")
    for row in m2:
        for col in row:
            print (f"{col} " , end=" ")
        print()    

# simple naive way
def  add2dMatrix(m1, m2) :
        sum = [
                [0, 0, 0],
                [0, 0, 0]
             ]
        for row in range(len(m1)): # row: 0 and 1 
            for col in range(len(m1[row])): # Col: 0 , 1 and 2  : Since three element in each row
                 sum[row][col] += m1[row][col] + m2[row][col]

        print("******* Sum of Above matrices - Result *********")
        for row in sum :
             print(row)      

# Usign numpy array:The numpy library has a built-in overload of the operator +, that allows one to perform the addition of matrices.
def add2MatFromNumpy(m1,m2):
     x = np.array(m1)      
     y = np.array(m2)
     r = x+y
     print("******* Sum By numpy - Result *********")
     print(r)


# using zip() funciton:
def add2MatFromNumpy(X, Y):
    result = [list(map(sum, zip(*t))) for t in zip(X, Y)]   
    print("******* Sum By zip() funciton - Result *********")
    for i in result:
       print(i)


matrix1 = [ 
            [1, 4, 2], 
            [3, 6, 8]
          ]

matrix2 = [ 
                [2, 2, 2], 
                 [2, 2, 2]
          ]

# lets print both the matrices in matrix form

printMatrices(matrix1, matrix2)
# lets add the above matrices
add2dMatrix(matrix1, matrix2)

add2MatFromNumpy(matrix1, matrix2)


# I/O:
'''
******* MATIRIX - 1 *********
1  4  2
3  6  8
******* MATIRIX - 2 *********
2  2  2
2  2  2
******* Sum of Above matrices - Result *********
[3, 6, 4]
[5, 8, 10]
******* Sum By numpy - Result *********
[[ 3  6  4]
 [ 5  8 10]]

'''

# FROM ZIP:
'''

Certainly! Let's break down the code step by step:

python
Copy code
# Program to add two matrices using zip()

# Define two matrices X and Y
X = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

Y = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Use zip to combine corresponding elements of X and Y
# and then use map and sum to add corresponding elements
result = [map(sum, zip(*t)) for t in zip(X, Y)]

# Print the result
print(result)
Explanation:

1-Matrix Definition:

Two matrices, X and Y, are defined. Each matrix is a list of lists, where each inner list represents a row of the matrix.

2-Zip to Combine Corresponding Elements:
zip(X, Y) combines the corresponding elements of the matrices. For each pair of corresponding rows (lists) in X and Y, a tuple is created.

3-Transposing with zip(*t):
zip(*t) transposes the tuples, effectively grouping the corresponding elements of each row together. This is a common technique to transpose a matrix in Python.

Mapping and Summing:
map(sum, ...) applies the sum function to each tuple, summing the corresponding elements of the transposed rows.

List Comprehension:
The outer list comprehension [...] iterates over the tuples obtained from zip(X, Y). For each tuple, it performs the transposition, mapping, and summing.

Printing the Result:
The result is printed. The final output is a list of lists representing the sum of the two matrices.
'''