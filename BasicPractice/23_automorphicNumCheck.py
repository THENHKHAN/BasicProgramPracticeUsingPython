
# Automorphic number using Python
# what actually it is ???
'''
A number is called an automorphic number if and only if the square of the given number ends with the same number itself. For example, 25, 76 are automorphic numbers because their square is 625 and 5776, respectively and the last two digits of the square represent the number itself.
Some other automorphic numbers are 5, 6, 36, 890625, etc.
'''
# Q- Check Whether or Not the Number is an Automorphic Number in Python



def isAutomorphicNumUsingEndWithFun(number) :
    sq = str(number **2)
    if (sq.endswith( str(number) ) ): # return true if it end with the specifeid string in the argument.
        return True

    return False

def isAutomorphicNumUsingSlicingOper (number) :
#EX:
# n = 376       ===> n^2 = 141376 141376[-3::] = 376    --- [-3::] similar to [-3:] --> include index -3,-2,-1 means last three char
   if int(str(number**2)[-len(str(number))::]) == number :
    return True
   else:
      False


n = int(input("\n\n Enter the number you want to check Automorphic number: "))

print("\n***********   Using Method-1 endwith() method of string    ***************\n")
print(f"YES, {n}  is an Automorphic number") if isAutomorphicNumUsingEndWithFun(n)  else print(f"NO, {n} is NOT an Automorphic number") 

print("\n***********   Using Method-2 SLICING OPerator method     ***************\n")
print(f"YES, {n}  is an Automorphic number") if isAutomorphicNumUsingSlicingOper(n)  else print(f"NO, {n} is NOT an Automorphic number") 




# methods:
'''
Method 1: Using Modulo Operators
Method 2: Short cut    -- slicing
Method 3: Using endswith() method
....etc.
note: remaing will be using later
'''



# Example:
'''
Input  : N = 76 
Output : Automorphic
Explanation: As 76*76 = 5776

Input  : N = 25
Output : Automorphic
As 25*25 = 625

Input : N = 7
Output : Not Automorphic
As 7*7 = 49
'''

# ALGO:
'''
How to find automorphic number?
Follow the steps given below:

1-->Read a number (num) from the user.
2--> Find the square of the given number and store it in a variable (square).
3--> Find the last digit(s) of the square.
4--> Compare the last digit(s) of the variable with num.
     i) If they are not equal, the given number is not an automorphic number.
    ii) If they are the same, go to the next step.
5--> Remove the last digit of the given number i.e. num.
6--> Repeat steps 4 to 6 until the given number becomes 0.

'''
# OR
'''
Algorithm:-
1---> Calculate the square of the number
2---> Extract digits of the square from the end
3---> If end digits and the number become equal at some point
4---> Then its an automorphic number
'''