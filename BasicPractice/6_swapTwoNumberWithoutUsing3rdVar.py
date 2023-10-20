
# Python program to swap two numbers without using third variable


def swapNum2 (num1 , num2 ) : # mehtod-2 by using simple arithemetic operation.lets say 10 , 20
    num1 = num1 + num2  # 10+20 = 30 => num1 = 30
    num2 = num1 - num2  # 30 - 20 => num2 = 10 - num2 values is swapped
    num1 = num1 - num2  # 30 - 10 => num1 = 20 - num1 values is swapped

    print (f"num1 : {num1} and num2 : {num2}")




# METHOD-1 - Easiest one
def swapNum1 (num1 , num2 ) :
    num1 , num2 = num2 , num1 # by this num2 value goes to num1 and vice -versa

    print (f"num1 : {num1} and num2 : {num2}")


num1 = int (input("Please enter you 1st number : "))
num2 = int (input("Please enter you 2nd number : "))

print (f"******* BEFORE SWAPPING *********")
print (f"num1 : {num1} and num2 : {num2}")
print (f"******* AFTER SWAPPING METHOD -1 *********")
swapNum1 (num1 , num2 ) # METHOD-1 
print (f"******* AFTER SWAPPING METHOD -2 *********")
swapNum2 (num1 , num2 ) # METHOD-2 




# INFO:
'''
we will learn to write a python program that will swap the numbers without introducing any new variable. Here, we will use two different approaches to do so.
In the first method, we will simply exchange the values and assign them to the two variables. In the second method, we will use some of the arithmetic operations 
like addition and subtraction to get the output as swapped numbers.
'''

# Mehtod-1
''' Here we'll just exchange their value. In python we can exchange value  '''