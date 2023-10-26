# Python Program to find sum of digits
# Way of Doing
'''
Here are three approaches, you can use to print the sum of digits.

1 -> Using str() and int()
2 -> Using iteration
3 -> Using recursion
'''


# Method-1 : Using str()&int() : approach: input () return as string so the entered number be of type string. And as we know how print or get the eahc characters 
                        # of string (means with for loop and in operator) and extracted digit convert into int and store them and add them.

def strIntMethod (number) : #-- new to me But now understood
      sumfOfDig = 0 

      for dig in str(number) :
            sumfOfDig += int(dig)
      return sumfOfDig
            

# Method-2 : Using iteration --> used it earlier
def iterationMethod(number) :
    sumfOfDig = 0

    while(number != 0 ):          
            lastDig =  number % 10  # extracting last digit once at a time
            number = number // 10 # removing the last digit and remaing storing           
            sumfOfDig += lastDig         

    return sumfOfDig


# # Method-3 : Using recursion --> New for me But now understood
def recursionMethod(number) :
      if (number <= 0) : # it will run only if the number become 0 or less 
            return number 
      else :
            dig = number % 10 # extracting last digit once at a time
            return ( dig + recursionMethod (number // 10 ) )# // return integer i.e. omit dig after decimal
      
      




number =int(input('Enter your number: '))
print(f"METHOD-1 => Sum of the digits {number} : { strIntMethod(number)} ")
print(f"METHOD-2 => Sum of the digits {number} : {iterationMethod(number)}")
print(f"METHOD-3 => Sum of the digits {number} : {recursionMethod(number)}")




# INFO :
'''
->we will learn how to calculate the sum of all the digits of a given number. We will learn all the possible methods to do 
this program. We will be using recursive functions, loops, and type conversion for this program in Python.
->In type conversion, we will convert integer to string for getting each digit of the number. Before moving forward you must 
know what is a string.
->The program should take an integer number as an input from the user and print the sum of its digits. For example,
153 => 1+5+3 = 9
'''