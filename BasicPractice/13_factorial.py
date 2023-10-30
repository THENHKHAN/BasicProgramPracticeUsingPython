
# Python Program to find factorial of a number

# Method : 
'''
1-> using built-in math modul function - factorial
2-> using Loop or iteration
3-> Using recursion
'''

from math import factorial

# method-1
def getFactorial(number) :
    return factorial(4)


# method-2 
def getFactByIteration (number) :
    fact = 1
    if (number==0 or number == 1) :
        return 1
    else:
       while (number >= 1):
            fact = fact * number
            number -= 1
        
       # it will execute when while conditon beome false
       else:
           return fact
      
    


# method-3
def getFactByRecursion (number) :
    fact = 1
    if (number==0 or number == 1) : # terminating conditons
        return 1
    else:
           return number * getFactByRecursion (number-1)

# starting ...

n = int(input("Enter the desired number to find the factorial of: "))

if (n<0) :
    print(" factorial of a Negative number is not possible")
else :

    print ("*************  Using Buit-in Function    ****************")
    print(f" Factorial of {n} :  {getFactorial(n)}\n\n")

    print ("*************  Using Loop    ****************")
    print(f" Factorial of {n} :  {getFactByIteration(n)}\n\n")

    print ("*************  Using Recursion    ****************")
    print(f" Factorial of {n} :  {getFactByRecursion(n)}\n\n")



    

# About while and else block:
'''
The else block is only executed if the while loop exits normally(i.e., when the loop's condition becomes False)
 means no break statement used .

'''












#INFO:
'''
The factorial of a non-negative number is the product of all the integers from 1 to that number. Factorial of a negative number 
is not defined and the factorial of 0 is always 1.

For example, Factorial of 7 is: 1 x 2 x 3 x 4 x 5 x 6 x 7 = 5040
'''