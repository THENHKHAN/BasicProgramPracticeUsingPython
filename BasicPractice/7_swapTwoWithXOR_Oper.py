
# Using bitwise XOR swapping. Without using 3rd variable 


def swapTwoIntByXOR_Oper(num1 , num2  ) :
    num1 = num1 ^ num2  # num1 and num2 get converted into binary and one by one it done XOR and it result give decimal (resultant of binary conversion automatically)
    num2 = num2 ^ num1 
    num1 = num1 ^ num2
    print (f"num1 : {num1} and num2 : {num2}")
    # Operation perform on each pair of corresponding bits


num1 = int( input('Enter value of first number (num1): ') )
num2 = int( input('Enter value of second number (num2): ') )

print (f"******* BEFORE SWAPPING *********")
print (f"num1 : {num1} and num2 : {num2}")
print (f"******* AFTER SWAPPING *********")

swapTwoIntByXOR_Oper (num1 , num2 )


# OUTPUT 
'''

Enter value of first number (num1): 10
Enter value of second number (num2): 20

******* BEFORE SWAPPING *********
num1 : 10 and num2 : 20

******* AFTER SWAPPING ********* 
num1 : 20 and num2 : 10

'''

# BitWise operator always gives result after operation in decimal




# INFO 
'''
 We will use one of the bitwise operator i.e. XOR. This method only works for integers 
 and works faster because this method uses bit operation (for same values, output = 0 and for different values, output = 1 WHEN performs betweentwo bits).

'''
# WARNING : This method only works for Integer values.

# ABOUT bitWise Operation and operator 

'''
Does BitWise operator always gives results after operation in decimal form??????????????????????????????????

ANS: 
        No, bitwise operators do not always give results in decimal form. Bitwise operators perform operations on binary representations of data, 
        and the results are usually in binary form. However, when you print or display the results in most programming languages,
        they are typically shown in decimal (base-10) form by default.


'''

# There is one more method : Using the division and multiplication operator for swapping. We'll do later.