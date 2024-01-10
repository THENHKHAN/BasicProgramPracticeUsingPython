# Python Program for Reversal Algorithm for Array Rotation
'''
In this tutorial, you will learn about Reversal Algorithm to rotate an array in Python. 
The user will give an input d by which the elements of the array will be rotated. Let's understand it.
'''
# https://www.studytonight.com/python-programs/python-program-for-reversal-algorithm-for-array-rotation
# REASON: the main logic behind this algorithm is to reverse the array in parts to get the desired output.
'''
Input arr[] = [1, 2, 3, 4, 5, 6, 7], d = 2, n =7
A[] and B[] are parts of the array arr[]

Result: [3, 4, 5, 6, 7, 1, 2]
'''


# method-1
def EasyWayBySlicing(arr, d):
    a = arr[ :d]
    b = arr[d: ]
    c = [*b, *a]
    return c

# method-2
def slicingAndReverseFun(arr, d):
    a = arr[ :d]
    b = arr[d: ]
    a.reverse() # it reverse array and does not return anything
    b.reverse()
    c = [*a, *b]
    c.reverse()
    arr[::]= c
    return arr

# in suppport of ReversalALGO() function: Without predefined reverse function
def reverseArray(arr, start, end): # start , end willl be based on requirement and d variable
        #  end will be excluded
    while (start < end):
        # just swapping two varibale value using third variable temp
        temp = arr[start] # start === index       
        arr[start] = arr[end] # swapping start to end 
        arr[end] = temp   # end from start
        start += 1 # incrementing index by 1
        end -= 1 # decrementing by 1 from end as well

   

# method-3 : Without creating any new Array 
def ReversalALGO(arr, d):
    reverseArray(arr, 0, d-1) # will reverse 1st half i.e to the dth position means index= positon-1
    # print(arr) # [20, 10, 30, 40, 50, 60, 70]
    reverseArray(arr, d, len(arr)-1) #len(arr)-1 since index 0 to length-1: 2nd HALF revered
    # print(arr)  # [20, 10, 70, 60, 50, 40, 30] 
    # one more reverse
    reverseArray(arr, 0, len(arr)-1) 
    # print("final revere : ", arr) # [30, 40, 50, 60, 70, 10, 20]


arr = [1, 2, 3, 4, 5, 6, 7] #, d = 2, n =7
print("Original Array :  " , arr)
print("******************* METHOD - 1 Easy slice way : It does not modify the original one **********************************")
position = 2
print(f" After rotaion of {position} places Element Resultant Array: {EasyWayBySlicing(arr,position)}")


print("******************* METHOD - 2 Slicing way But have create 2 or 3 new array  **********************************")
print("Original Array :  " , arr)
print(f" After rotaion of {position} Element Resultant Array: {slicingAndReverseFun(arr,position)}")
print("Original Array Also modified:  " , arr)

print("******************* METHOD - 3 - reversal ALGO: Without creating any new Array  **********************************")
arr2 = [10, 20, 30, 40, 50, 60, 70] #, d = 2, n =7
print("Original Array :  " , arr2)
print(f" After rotaion of {position} Element Resultant Array: {ReversalALGO(arr2, position)}")
print("Original Array Also modified:  " , arr2)


'''
Original Array :   [1, 2, 3, 4, 5, 6, 7]
******************* METHOD - 1 Easy slice way : It does not modify the original one **********************************
 After rotaion of 2 places Element Resultant Array: [3, 4, 5, 6, 7, 1, 2]
******************* METHOD - 2 Slicing way But have create 2 or 3 new array  **********************************       
Original Array :   [1, 2, 3, 4, 5, 6, 7]
 After rotaion of 2 Element Resultant Array: [3, 4, 5, 6, 7, 1, 2]
Original Array Also modified:   [3, 4, 5, 6, 7, 1, 2]
******************* METHOD - 3 - reversal ALGO  **********************************
Original Array :   [10, 20, 30, 40, 50, 60, 70]
 After rotaion of 2 Element Resultant Array: None
Original Array Also modified:   [30, 40, 50, 60, 70, 10, 20]
'''