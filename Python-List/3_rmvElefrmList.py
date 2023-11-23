
# We'll be learning 3 things in this part:
'''
1 --> Remove an element (in general)----> # if ele is not present in the list then THROW ERROR:: ValueError: list.remove(x): x not in list
        SyntaX:
                lst.remove(element To Remove)    -- It returned nothing

2 --> Remove an element from END
        SyntaX:
                lst.pop()  -- it always remove the last element. And returned the removed element.
                Remark : If you try to pop from a empty list it will throw ERROR: IndexError: pop from empty list

3 --> Remove an element at a specified INDEX

        SyntaX: call del statement : https://docs.python.org/3/tutorial/datastructures.html#the-del-statement
                 del lst[INDEX]       -- its a statement to does not return anything.If you try it will throw EXCEPTION.

       0) if index is out of range then it will throw error: IndexError: list assignment index out of range

       i)  IMP*: There is a way to remove an item from a list given its index instead of its value: the del statement. This differs from the pop() method
                which returns a value. The del statement can also be used to remove slices from a list or clear the entire list (which we did earlier by assignment
                of an empty list to the slice). 

       ii)  del can also be used to delete entire variables: del lst   

       EX: 
       a = [-1, 1, 66.25, 333, 333, 1234.5]
            del a[0]
            print(a)
            [1, 66.25, 333, 333, 1234.5]
            del a[2:4]
            print(a)
            [1, 66.25, 1234.5]
            del a[:]
            print(a)
            []
'''


# 1   - remove "banana" from the list
def rmvEleFromList(lst) : # remove() method
    eleToRmv = "bananas"
    if ( eleToRmv in lst ): # bcz it might be possible that element not in the list so checking 1st
        lst.remove(eleToRmv)  
        print(f"List after removing bananas : {lst}") # ['apples', 'oranges', 'mangoes', 'grapes', 'strawberry']
    else:
        print(f"Element {eleToRmv} is not present in the list")

# 2  - remove Last Element from the list
def rmvEleFromEndOfList(lst) : # pop() method
    if len(lst) == 0 : # it is similar to lst == [] 
        print("List is Empty you can't pop/remove any element from that.")
        
    else:
        rmvdEle= lst.pop()
        print(f"List after removing LAST element : {lst}") # ['apples', 'oranges', 'mangoes', 'grapes']
        print(f"Removed elelment is : {rmvdEle}")  # Removed elelment is : strawberry


def rmvEleAtSpecifiedIndexFromList (lst) : # del statement
    ind = 2 # for single index 
    # ind = [1:4]
    if (len(lst) == 0 ) :
        print("List is Empty you can't delete any element from that.")
 
    elif (ind >= len(lst) or ind < -(len(lst))) : # checking for index one is greater or equal to lst size i.e + index and other les that negative index
       print("Index out of Bound ")
        
    else:
      del lst[1:4]  # ind 
      print(f"List after removing Element at INDEX 1 to 4-1  : {lst}")
    #     List after removing Element at INDEX 1 to 4-1  : ['apples']



thisList = ['apples','oranges','bananas','mangoes','grapes','strawberry']
print(f" ORIGINAL LIST : {thisList}")
rmvEleFromList(thisList)
rmvEleFromEndOfList(thisList)
rmvEleAtSpecifiedIndexFromList(thisList)

# I/O
'''
 ORIGINAL LIST : ['apples', 'oranges', 'bananas', 'mangoes', 'grapes', 'strawberry']
List after removing bananas : ['apples', 'oranges', 'mangoes', 'grapes', 'strawberry']
List after removing LAST element : ['apples', 'oranges', 'mangoes', 'grapes']
Removed elelment is : strawberry
List after removing Element at INDEX 1 to 4-1  : ['apples']

'''