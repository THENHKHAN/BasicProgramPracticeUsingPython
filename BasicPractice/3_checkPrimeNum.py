# Program to Check for Prime Number

def checkPrimeNo (inputNum):
    if (inputNum <= 1 ) :
        print("prime number Not possible")
        return
    else:
        check = 2
        while(check < inputNum ) :
            flag = False
            if (inputNum % check == 0) :
                print("{} is not a prime Number ".format(inputNum))
                break
            else:
                check += 1
        
        else :
            print (" {} is a Prime Number ".format(inputNum))

userNum = int ( input( "Enter your number : " ))
checkPrimeNo(userNum)

# INFO 

'''
We'll learn how to check if a number is prime or not using Python Programing language. 
Our program should take a number given by the user and display if it is prime or not.
'''
# Approach 
'''
We will use for loop and if-else conditional statements for executing this program. Before moving further it is necessary that you have some knowledge about conditional statements in Python. For example,

The program should take the following as input and give output accordingly,

Input- Enter number: 4

Output- 4 is not prime
'''
# format() for variable substitution inside string 
'''
The format() is a function for handling strings that permits you to do variable substitutions and data formatting. Here we have used this function
 to print the value of num. This function will print the value where {} is present.
'''