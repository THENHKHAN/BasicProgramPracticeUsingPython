
# Python Program to Interchange First and Last Elements in list
'''
Input : [14, 3, 56, 17, 8, 10]
Output : [10, 3, 56, 17, 8, 14]
'''

def interChange1stAndLastEleOfList( lst) :# using indexing and a temp variable
    lstLen = len(lst)
    temp = lst[0]  
    lst[0] = lst[-1] # or lst[0] = lst[lstLen-1]
    lst[-1] = temp # lst[lstLen-1] = temp
    # OR
    # lst[0] , lst[-1] = lst[-1] , lst[0]

def usingPopMethod(lst):# using pop () method - by default pop() is pop(-1) means last element- It remove the element and returned the removed element
    first = lst.pop(0)
    last = lst.pop(-1)
    lst.insert(0,first)
    lst.insert(-1,last)



myList = [14, 3, 56, 17, 8, 10]
print(f"ORIGINAL LIST: {myList}")

interChange1stAndLastEleOfList(myList)

print(f"Updated list By method-1 - indexing & third variable: {myList}" )

usingPopMethod(myList)
print(f"Updated list By method-2 pop&insert method: {myList}" )
