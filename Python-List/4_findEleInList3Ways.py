
# Python Program to check if element exists in list

# Problem:
'''
The program will accept the list and the element which has to check, it should return True if it exists else, it will return False
Input: [6, 22, 7, 3, 0, 11] element= 0
Output: True
'''
# Approach To Find Element
# IWe will be discussing the three main methods for checking if an element exists in a list.
'''
1---> Comparing each value in the list to the element.
2---> Using in operator to check for an element in the list.
3---> Using count(ele) list method to count the number of times an element is present.
Let us look at each approach separately
'''

# method-1 Naive - Looping

def findEle1 (lst , ele):
    for x in lst :
        if (x == ele) :
            return True
        else :
            False

# method-2 - Python way - using in operator
def findEle2 (lst , ele):
    if ele in lst:
        return True
    else:
        False


# method-3 - Python way - List method count()-The count() method returns the number of elements with the specified value.
def findEle3 (lst , ele):
    count = lst.count (ele) # it will find how many time that provided element is occur in the given list
    if (count > 0) :
        print(f"element-{ele} ouccurs {count} times")
        return True
    else:
        return False
    

# method-4 - Advance - using loop doing same as findEle3()doing -May be more than one times element got then counting as well as checking
def findEle4 (lst , ele):
    counter = 0
    for x in lst :
        print(f"Val : {x}")
        
        if (x == ele) :
            counter += 1
            print(f"counter : {counter}")
        else:
            pass
    else:
        if (counter > 0 ) :
            print(f"element-{ele} ouccurs {counter} times")
            return True
        else:
            return False




def checkResult (chk):
    if (chk) :
        print ("Yes, ELement found!!")
    else:
        print ("ELement NOT found!!")


myList =[6, 22, 7, 3, 0, 11 ,22, 23, 11, 11, 3, 33, 100, 22,]
print(f"LIST: {myList}")
print("Enter the element that want find/check in the above list: " , end="")
inp = int (input () )

print("**************** method-1 Naive - Looping     *************************")
#m-1
chk = findEle1(myList,inp)
checkResult(chk)


print("**************** method-2 Python Way - in Operator     *************************")
#m-2
chk = findEle2 (myList , inp)
checkResult(chk)

print("**************** method-3 Python Way - it.count(ele) Method     *************************")
#m-3 
chk = findEle3(myList,inp)
checkResult(chk)

print("**************** method-4 My Way -looping+counting - same approach as method-3  *************************")
#m-4 
chk = findEle4(myList,inp)
checkResult(chk)



#IMP:about count()
'''
The count method is a built-in method in Python that can be applied to certain iterable types. 
Its purpose is to count the occurrences of a specified value within the iterable.

So, while the count method is commonly used with lists, it can also be used with strings and tuples, 
but not with dictionaries directly. For dictionaries, you might need to use other methods or perform specific operations based on your needs.

'''

