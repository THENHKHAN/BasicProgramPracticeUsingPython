
# Remove multiple elements from a list in Python
#INFO:
'''
Elements in a list can be deleted based on certain conditions or by specifying the range of their indexes.

First, we will see how to delete elements based on a condition.

***Condition: Numbers that are divisible by 5 should be deleted from the list.

### For example, given a list of numbers, you have to remove all those elements from the list which are divisible by 5.

Input: [10, 3, 12, 15, 5, 8]
Output: [3, 12, 8]

To solve this problem, we can follow these approaches:

For removing multiple elements from a list based on a certain condition, we can follow these approaches-
1----> Remove multiple elements from a list while Iterating.
2----> Remove multiple elements from a list using List Comprehension.
3----> For removing multiple elements from a list by index range we can use del operator.
'''

# m-1 -iterating
def usingIteratingMethod(lst,conEle):
    
    for ele in list(lst): # list(lst) bcz  every time list change(lst varible).it reduces index so by list(lst) ele will extract from new list i.e list(lst) not lst.
        # print(ele,end=" ")
        if ele % conEle == 0:
            lst.remove(ele)  
            # print("lst: " , lst)
    else:
        return lst # original list will be chnage bcz list is a mutable object
    
# m-2 : generating new list with only satisfied conditon with list comprehension
def listComprehension(lst,conEle):
    newLst = [ele for ele in lst if (ele % conEle ) != 0] # excluding which are not divisible by 5
    return newLst


def filteringWay (lst ) :
    print("list for filtering -LIST: " , lst)
    print("Removing element from above list which are not divisible by 2: ")
    newList = list( filter(lambda ele : ele % 2 != 0 , lst) )
    print(f"Updated LIST: {newList}")

myList = [5, 55, 10, 35, 25, 20, 2,10, 3, 12, 15, 5, 8]
print(f"ORIGINAL LIST: {myList}")
print(f"************************************* METHOD-1 -- Iterating ************************************* ")
print("remove all those elements from the list which are divisible by 5.")
print(f"Updated LIST: {usingIteratingMethod(myList,5)}")
myList.extend([5,10,100]) # it used to add muliple element at one but take only arg that's y given bounded list
print(f"************************************* METHOD-2 -- list comprehension ************************************* ")
print(f"LIST: {myList}")
print("remove all those elements from the above list which are divisible by 5.")
print(f"Updated LIST: {listComprehension(myList,5)}")
filteringWay(myList)