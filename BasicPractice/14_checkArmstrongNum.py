
# Python Program to Check Armstrong Number

#INFO: A positive integer having n digits is Armstrong if, the sum of the digits raised to the power n is equal to the number.

# EX: 
'''
For a 3 digit number, we can say that a number is an Armstrong if the sum of the cubes of a number is equal to the number itself.

Suppose the number is 153 then,

1³ + 5³ +3³ = 1 + 125 + 27 = 153

Since the sum of cubes is 153 the number is Armstrong number.
'''

def TotalNumOfDigInNumber(number) :# calculating total number of digit in the number
    totalDig=0
    while(number > 0 ):
        totalDig += 1
        number = number // 10
    else:
        return totalDig
# another way of doing the above one : totalDig = len(str(n))- without using any extra function

def checkArmstrong (number) :
    totalDig=  TotalNumOfDigInNumber(number)
    tempNum = number
    sum = 0
    while (number > 0):
            dig = number % 10 
            number = number // 10 
            sum += dig ** totalDig

    if(tempNum == sum):
        return True
    else:
       return False


n = int(input("Enter the number to check for ArmStrong number: "))

if (n<0) :
    print(" Armstrong of a Negative number is not possible")
else :
   
   check =  checkArmstrong(n)
   if (check) :
       print(f"Yes, {n} is an Armstrong number")
   else:
       print(f"NO, {n} is Not an Armstrong number")