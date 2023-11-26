
# Python program to print even and odd numbers in a list
'''
Input: [13, 17, 9, 8, 15, 29, 20, 41, 74]
Output: 
 List of EVEN number : [8, 20, 74]
 List of ODD number : [13, 17, 9, 15, 29, 41]

'''

def printEvenNum(lst):
    evenList = []
    oddList = []
    for ele in lst :
        if (ele % 2 == 0):
            # print("Even-> "  , ele , end = " ")
            evenList.append(ele)
        else :
            # print("odd-> "  , ele , end=" ")
            oddList.append(ele)

    else: # it will execute only after for loop execute completely without any break statement
        return evenList , oddList # returning two variable through funtion


myList = [13, 17, 9, 8, 15, 29, 20, 41, 74]
print(f"Orinal List : {myList}")
even , odd = printEvenNum(myList)
print(f" List of EVEN number : {even}")
print(f" List of ODD number : {odd}")

