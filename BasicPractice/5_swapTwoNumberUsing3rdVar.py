
# Program : Swap two number using 3rd variable

def swapNum (num1 , num2 ) :
    temp = num1 # it will store temprary value of number so that num1 can be modified and original value preserve.
    num1 = num2
    num2 = temp
    print (f"num1 : {num1} and num2 : {num2}")



num1 = int (input("Please enter you 1st number : "))
num2 = int (input("Please enter you 2nd number : "))

print (f"******* BEFORE SWAPPING *********")
print (f"num1 : {num1} and num2 : {num2}")
print (f"******* AFTER SWAPPING *********")
swapNum (num1 , num2 )

# INFO 

'''
we will learn to write a python program that will swap the numbers using a third variable. Here, 
we will take temp as the third variable such that we will use the temp variable to temporarily store the first number's value.

As the output, we are required to get the swapped numbers.

'''
# I/O
'''

Please enter you 1st number : 10
Please enter you 2nd number : 20
OUTPUT:
******* BEFORE SWAPPING *********
num1 : 10 and num2 : 20
******* AFTER SWAPPING *********
num1 : 20 and num2 : 10

'''