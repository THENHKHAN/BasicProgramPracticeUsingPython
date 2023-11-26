
# Python program to print all even and odd numbers in a range - user choice lower and upper limit of range.
'''
Input: lower limit= 4
upper limit= 10
Output: even : 4 6 8 10
        odd  : 5 7 9
'''

def usingSimpleLoop(l,u):
    evenNum = []
    oddNum = []
    myList = []
    for ele in range(lowerLim , upperLim+1):
        myList.append(ele)
        if (ele % 2 == 0):
            evenNum.append(ele)
        else:
            oddNum.append(ele)

    print(f" Generated LIST : {myList}")
    print(f" List of EVEN number : {evenNum}")
    print(f" List of ODD number : {oddNum}")


lowerLim = int(input("Pease enter lower limit: "))
upperLim = int(input("Pease enter upper limit: "))
usingSimpleLoop(lowerLim,upperLim)
myList = [ele for ele in range(lowerLim,upperLim+1)] #list comprehensive way to generate list
print(myList)
