# Python program for Reversing a List
'''
I = [1, 2, 3, 4, 5, 6, 7]
O = [7, 6, 5, 4, 3, 2, 1]

'''

# m-3=> In this approach, we will declare a new list and then use the slicing operator (:) to copy the elements in reverse order in the new list.
# using new list with -neg index reversed-It does not modified existing instead it  creating new list object and storing in a varible

def reveredList (lst) :
        emptList = lst[ : :-1] 
        return emptList



# m-1==> Using reverse() method
def usingReversedMethod(lst):
        # newList = reversed(lst) #-- it returned a list object and can print revered list and we can using for loop and apend method to reasing the elemnet from newList 
        # print(newList)
        # for i in newList:
        #         print(i , end =" ")
        lst.reverse()
        return  lst


# m-2 ==>  Two pointer Approach : It modify the existing list-So Efficient
def twoPointerApproach(lst) :
        start = 0
        end = len(lst)-1
        while(start <= end) :
                lst[start] , lst[end] = lst [end] , lst[start]
                start += 1
                end += -1
        return lst


myList = [1,2,3,4,5,6,7,8]
print(f"ORIGINAL LIST: {myList}")
print(f" Method-1 : revered()method : {usingReversedMethod(myList)}")
print(f" Method-2 : Two pointer Approach : {twoPointerApproach(myList)}")
print(f" Method-3 : new list created : {reveredList(myList)}")

# I/O
''

ORIGINAL LIST: [1, 2, 3, 4, 5, 6, 7, 8]
 Method-1 : revered()method : [8, 7, 6, 5, 4, 3, 2, 1]
 Method-2 : Two pointer Approach : [1, 2, 3, 4, 5, 6, 7, 8]
 Method-3 : new list created : [8, 7, 6, 5, 4, 3, 2, 1]'

'''