# Python Program to check if given array is Monotonic
# IMP: An array with only a single element will be treated as a monotone and the function should return the value True in our program.
# INFO
'''
We will learn how to check if an array is monotone or not. An array is a container data structure that stores elements, where each element can be accessed by an index. 
An array is said to be monotonic in nature if the array elements are continuously increasing or continuously decreasing.
'''
# The all() function returns True if all items in an iterable are true, otherwise it returns False.
# If the iterable object is empty, the all() function also returns True.

# def isMonotonic(lst):
    

#  took hint
def ismonotone(a):
    n=len(a) #size of array
    if n==1 or a == []:
        return True
    else:
        #check for monotone behaviour
        if all(a[i]>=a[i+1] for i in range(0,n-1) or a[i]<=a[i+1] for i in range(0,n-1)):
            return True
        else:
            return False

# my way-1
def fun1(a):
    flag  = False
    if len(a) ==1 or a == []:
        return True
    
    else:
        if a[0] >= a[1]:
            for i in range(0,len(a)-1):
                if a[i]>=a[i+1]:
                    flag = True
                else:
                    return False
        else:
            for i in range(0,len(a)-1):
                if a[i] <= a[i+1]:
                    flag = True
                else:
                    return False
        return flag

# my way-2
def fun2(a) :
    if len(a) ==1 or a == []:
         return True   
    else:
        inc = [True if (a[i]>=a[i+1]) else False for i in range(0,len(a)-1)]
        dec = [True if (a[i]<=a[i+1]) else False for i in range(0,len(a)-1) ]
        print(inc)
        print(dec)
        if all(inc) and len(inc) == len(a)-1 :
            return True
        elif all(dec) and len(dec) == len(a)-1:
            return True  
        else:
            return False
        

        
A = [6, 5, 4, 2]
print("******************* LIST-1   **********************************")
print("1st list :  " , A)
print(f"Method-0 ")
# print(ismonotone(A)) for reference
print(f"Method-1 ")
print(fun1(A))
print(f"Method-2 ")
print(fun2(A))

print("******************* LIST-2   **********************************")

b = [6, 2, 4, 2]
print("2nd list :  " , b)
print(f"Method-0 ")
# print(ismonotone(b))
print(f"Method-1 ")
print(fun1(b))
print(f"Method-2 ")
print(fun2(b))

print("******************* LIST-3   **********************************")



c=[2,3,4]
print("3rd list :  " , c)
print(f"Method-0 ")
# print(ismonotone(c))
print(f"Method-1 ")
print(fun1(c))
print(f"Method-2 ")
print(fun2(c))

print("******************* LIST-4   **********************************")


d=[1]
print("4th list :  " , d)
print(f"Method-0 ")
# print(ismonotone(d))
print(f"Method-1 ")
print(fun1(d))
print(f"Method-2 ")
print(fun2(d))

print("******************* LIST-5   **********************************")


e=[]
print("5th list :  " , e)
print(f"Method-0 ")
# print(ismonotone(e))
print(f"Method-1 ")
print(fun1(e))
print(f"Method-2 ")
print(fun2(e))







# arr = [1, 2, 3, 4, 7, 10]



# Monotonic increasing:
'''
An array A[] is monotonic increasing if all the elements in it satisfy the condition
for all i <= j, A[i] <= A[j]
[1, 2, 3, 4, 7, 10] is monotonic increasing.
'''

# Monotonic decreasing:
'''
An array A[] is monotone decreasing if all the elements in it satisfy the condition:
for all i <= j, A[i] >= A[j]
[11, 10, 9, 6, 4, 1] is monotonic decreasing.
The program should take the array as input and return True if the array is monotonic else it should return False. For example,
'''
# Look at the sample input and output for the program.
'''
Input: 7 3 2 1 0
Output: True

Input: 10 11 13 9 14
Output: False
'''

# We will follow the approach of checking if the array is monotonic increasing or decreasing by checking the adjacent elements in the array. 

'''
To check for monotonic increasing, we will check if a[i]<= a[i+1] for all indexes i from 0 to n-1 where n is the size of the array. 
To check for monotonic decreasing, we will check if a[i]>= a[i+1] for all indexes i from 0 to n-1 where n is the size of the array.
'''
# V.V.V IMP ==> An array with only a single element will be treated as a monotone and the function should return the value True in our program.

# Algorithm
'''
Look at the algorithm to understand the working of the program.
Step 1- Define a function that will check the monotone nature of the array
Step 2- Find and store size of array using len()
Step 3- If the array has only one element return True
Step 4- Else, check if all values in the array are continuously decreasing or continuously increasing
Step 5- If the condition is true, return True
Step 6- If the condition is not true, return False
Step 7- Declare an array with values
Step 8- Pass the array in the function
Step 9- Print the result

'''