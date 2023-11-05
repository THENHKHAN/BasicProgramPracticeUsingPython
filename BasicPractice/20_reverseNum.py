

# Find the Reverse of a Number in python 
# way of doing this: slicing , list with reverse() then join , looping, recursion
# ex:
'''
Example
Input : 123
Output : 321
'''

# Approach
'''
Given a integer input the objective is to break down the  number into digits and rearrange them in reverse order. 
We'll use loops and recursion to reverse the number input.
logic - expand the given number and search for logic:
123 = 1X100 + 2X10 + 3X1   as we can see from the last digit to 1st 10 to the power incresing by 1 and starts from 0 goes to numberOf input dig-1.Means  positional numeral system 0 ten hundres thousand etc places.
In the above logic we have to write another function to find the number of digit then we have mulitply each extracted digit from last to 1st from total number of digit in this way:
digX10 to the power numberOfDig-1 and decrese in each loop since we need to change their position thats why -1 each time
3X100+2X10+1X1.
But in the below method we doing the same but in more efficient way-multiply by 10 so that each position of number incre mean -1-10-100-1000:once 10s 100s..
'''

def reverTheNum(num) :

    reversedNum = 0
    while(num > 0): 
        dig = num % 10 # extracting each digit one by one
        reversedNum = reversedNum * 10 + dig # multiplying by 10 bcz we  are dealing with decimal number system which has base 10.
        num //=10 
    else:
         return reversedNum

def  reversedMyNum(num , reversedNum=0) :
    if (num == 0) :
        return reversedNum # control varible
    else:
        dig = num % 10
        reversedNum = reversedNum*10 + dig
        return reversedMyNum(num//10 , reversedNum) # recursion call
    

num = int (input("Please enter your number : "))

print("\n*********** 1- Using LOOP ***********")
myReverNum=reverTheNum(num)
print(f"The reversed number of above is : {myReverNum}")
print("\n *********** 2- Using Slicing Operator ***********")
rvrNum = str(num)[::-1] # it will get reverse order. -1 is showing to get in reverse order
print(f"The reversed number of above is : {int(rvrNum)}")

print("\n *********** 3- Using Recursion ***********")
myReverNum=reversedMyNum(num)
print(f"The reversed number of above is : {myReverNum}")



# explanation:
'''
Read for MORE: https://prepinsta.com/python-program/to-find-the-reverse-of-a-given-number/

In a positional numeral system, each digit's position represents a power of the base. In the decimal system, the base is 10, and the positions are powers of 10. For example, in the number 123:

The rightmost digit (3) represents 3 * 10^0 (which is 3).
The middle digit (2) represents 2 * 10^1 (which is 20).
The leftmost digit (1) represents 1 * 10^2 (which is 100).
So, when you reverse the number 123 digit by digit, you essentially extract and rearrange the digits, applying the reverse positional values:

1-->You start with reverse = 0.
2-->Then, you remove the last digit from the original number (num = 12), and you continue.
3-->You extract the next digit (2) and add it to reverse as reverse = reverse * 10 + 2, which sets reverse to 32.
4-->You extract the last digit (3) and add it to reverse as reverse = reverse * 10 + 3, which sets reverse to 3.
5-->You remove the last digit from the original number (num = 1), and you continue.
6-->You extract the final digit (1) and add it to reverse as reverse = reverse * 10 + 1, which sets reverse to 321.
   
    Finally, you remove the last digit from the original number (num = 0).
    At this point, you have reversed the number, and reverse holds the value 321, which is the reverse of the original number 123.

'''