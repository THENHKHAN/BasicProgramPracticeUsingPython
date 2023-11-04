

# Program to check if the number is a Harshad number or not.
'''
--> A Harshad number (or Niven number) is a positive integer that is divisible by the sum of its digits.
--> In other words, a number is a Harshad number if it is evenly divisible by the sum of its digits exactly.
--> For example, 18 is a Harshad number because 1 + 8 = 9, and 18 is divisible by 9.

'''

def checkHarshadNumber (number ) :
        sumOfDig = 0
        tempStrg= number
        # lets extract all the digit of the given number
        while(number > 0) :
                dig = number % 10 # it will extract the digit one by one from last digit to 1st
                sumOfDig += dig # collecting and making sum of digits
                number //= 10 # removing the digit from the given number which already extracted
        else:# this part will execute when while loop executed completely
                if (tempStrg % sumOfDig == 0):
                      return True
                else:
                     return False
        

num1 = int (input("Please enter you number that you wanna check : "))

try:
    check = checkHarshadNumber(num1)
    if (check):
        print(f"YES, {num1} is a Harshad Number")
    else:
        print(f"NO, {num1} is NOT a Harshad Number")
except Exception as e:
     print("There is a problem : ",e)
     print("kindly try some different number")
     

          



'''
    
    Ex- Number is 21

it is divisible by its own sum (1+2) of its digit(2,1)

So it is Harshad's Number

Some other Harshad's Number are 156,54,120 etc
    
'''