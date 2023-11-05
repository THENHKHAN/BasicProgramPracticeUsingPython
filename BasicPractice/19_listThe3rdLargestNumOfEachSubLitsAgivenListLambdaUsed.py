# https://www.javatpoint.com/python-lambda-functions

# Code to print the third-largest number of the given list using the lambda function
""" Using Lambda with Multiple Statements  """

# info :
'''
Multiple expressions are not allowed in lambda functions, but we can construct 2 lambda functions or more and afterward call the 
second lambda expression as an argument to the first. We are sorting every sub-list from the given list in the below program. 
Let us use lambda to discover the third largest number from every sub-list.
'''
# example:
'''  [ [3, 5, 8, 6], [23, 54, 12, 87], [1, 2, 4, 12, 5] ]  ====>  The third largest number 
from every sub list is: [5, 23, 4] '''


# Question : Print the third-largest number of the given list using the lambda function

''' Lets use MOST concise way: using lamda and List Comprehension function WAY '''
def byUsingLamdaWayAndListComprehension(lst):
    # thirdMaxValueOfEachList = []

    sortedList = lambda row: sorted(row)
    thirdLargestNum = lambda myOriginalList: [sortedList(extractedRow)[-3] for extractedRow in myOriginalList]
    """ sorting each row of 2d list by calling sortedList function.and from then returned list extracting last 3rd index since this would be the 3rd largest 
        and then making new list with lis comprehension way that will contain all 3rd max number of each subList.
    """
    thirdMaxValueOfEachList = thirdLargestNum(lst) # In this lambda function will call another lambda function in list comprehension.
    return thirdMaxValueOfEachList


''' Lets use more concise way: using lamda and map() function WAY '''
def byUsingLamdaWithMapFunWay(lst):
    thirdMaxValueOfEachList = []
    sortedList = lambda row: sorted(row)  # sorting each row and returning a new sorted list
    map_itr = map(sortedList, lst)
    for row in map_itr:
        print(row, end="\n")
        thirdMaxValueOfEachList.append(row[len(row) - 3])  # === row[-3]

    return thirdMaxValueOfEachList


'''By Using my own 1st logical way'''
# Approach
'''
1-> Extracted each row from a given 2d or list of list of int
2-> Sorted each row using sort() method in ascending order
3-> Appended in a empty LIST the 3rd largest number using NEGATIVE Indexing.

'''


def getThe3rdLargestNumberInTheGivenList(lst):
    count = 0
    thirdMaxValueOfEachList = []
    # lets sort each row
    for row in lst:
        count += 1
        print(count, end="row: ")
        row.sort()  # it modified the existing list
        print(row)
        thirdMaxValueOfEachList.append(row[-3])
    print("*** SORTED LIST ***")
    for row in lst:
        for col in row:
            print(col, end=" ")
        print()
    return thirdMaxValueOfEachList


# or 2d Array - array of array of Int or list of list of in= list[list][int]
# or find the 3rd largest number from each row if a given LIST.
myList = [[3, 5, 8, 6],
          [23, 54, 12, 87],
          [1, 2, 4, 12, 5]
          ]

print(f"Here is the origin list: {myList}")
print("In Matrix Format")
for row in myList:
    for col in row:
        print(col, end=" ")
    print()

print("*********** 1- My OWN Logic way ***********")
myDesiredList = getThe3rdLargestNumberInTheGivenList(myList)
print(f"3rd Max list of values from the above : {myDesiredList}")

print("*********** 2- Using Lambda with map() function way ***********")
myDesiredList = byUsingLamdaWithMapFunWay(myList)
print(f"3rd Max list of values from the above : {myDesiredList}")

print("*********** 3- Using Lambda with List Comprehension way ***********")
myDesiredList = byUsingLamdaWayAndListComprehension(myList)
print(f"3rd Max list of values from the above : {myDesiredList}")

# Some new  things learnt from this question:
'''
--> sort() method:
https://www.freecodecamp.org/news/python-sort-how-to-sort-a-list-in-python/
sort() method returns None, which means there is no return value since it just modifies the original list. It does not return a new list.

--> Diff b/w sort()method  and sorted() function
        The main difference between sort() and sorted() is that the sorted() function takes a list and 
        returns a new sorted copy of it.
'''
