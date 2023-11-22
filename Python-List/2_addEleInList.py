
# In this we'll be learning how to add element in a given list. At the end and at any user desired index.
'''At the end: we'll use append method to add element from the end of the list'''
'''At the any INDEX: In this we'll use INSERT method , it take two params (indexNum , element) - 
IMP: It implicitly adjust other element indices '''

# add element from the end of a list
def addEleFromEnd(lst , ele) :
    print("One Item adding at END using append() method ")
    lst.append(ele)
    # return lst # updated list will be returned  -- DONT need to return since LIST is mutable so it will udate in the existing list
def addEleAtAnyIndex (lst , index , ele) :
    print(f"One Item adding at INDEX-{index} using insert() method ")
    lst.insert(index , ele)
    # return lst # updated list will be returned from this function -- DONT need to return since LIST is mutable so it will udate in the existing list


myOriginalList = [1,2,5,88,100,13]
print("***********  Origin List         **************")
print(myOriginalList)
ele = input("Enter element that you want to add : ")

addEleFromEnd(myOriginalList,ele)
print("***********  Updated Original List         **************")
print(myOriginalList)

ind = int(input("Enter at which index you want add element: "))
addEleAtAnyIndex(myOriginalList,ind,ele)
print("***********  Updated Last List         **************")
print(myOriginalList)


# INPUT/OUTPUT:
'''

***********  Origin List         **************
[1, 2, 5, 88, 100, 13]
Enter element that you want to add : 44
One Item adding at END using append() method 
***********  Updated Original List         **************
[1, 2, 5, 88, 100, 13, '44']
Enter at which index you want add element: 3
One Item adding at INDEX-3 using insert() method 
***********  Updated Last List         **************
[1, 2, 5, '44', 88, 100, 13, '44']


'''