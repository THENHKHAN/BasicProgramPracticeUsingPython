
# Python Program to find LCM/LCD in python 

#INFO:
'''
The least common multiple/divisor (L.C.M. aka LCD ) of two numbers is the smallest positive integer that is perfectly divisible by the two given numbers.
multiple means :
4 -> 4 , 8 ,12 , 16 ,20 , 24 ,28 ,....
6 -> 6 ,12 ,18 ,24 , 30 ......
Hence LCM of 4 and 6 => 12 since 12 is the least/lowest common multiple
'''
# Conclusion/Analysis:
'''
Least largest common multiple would be a*b  except 1.
Now since LCM must be divisible by both the number (a and b) So here we can draw one more conclusion that we should start checking after or from 
the larger number b/w the two provided number.It will save some time.


'''

from math import lcm

# The lcm function was newly introduced in the Python version 3.9.0.
def getLcmByBuilt_inFun(n1,n2) :
        myLcm = lcm(n1,n2)  # buit-in function
        return myLcm


def getLCMbyLinearInteration (num1,num2):  # Method 2: A linear way to calculate LCM. By Looping Or most ordinary way
        greaterNum = num1
        if (num1 == num2 ):
                return num1
        elif(num1 > num2 ) :
                greaterNum = num1
        else :
                greaterNum = num2

        for lcm in range(greaterNum , num1*num2 +1):
                if (lcm % num1 == 0  and lcm % num2 == 0) :
                        return lcm
                else:
                        pass





num1 = int (input("Please enter you 1st number : "))
num2 = int (input("Please enter you 2nd number : "))

print(f"The L.C.M. of {num1} and {num2} : {getLcmByBuilt_inFun(num1, num2)}" )
print(f"The L.C.M. of {num1} and {num2} : {getLCMbyLinearInteration(num1, num2)}" )


#IMP INFO:
'''
1-> The Least Common Multiple (LCM) of a group of numbers is the least possible number that is divisible by all the numbers in the group.
2-> for more : https://www.educative.io/answers/what-is-the-mathlcm-function-in-python
        
'''
#I/O
'''
Please enter you 1st number : 54
Please enter you 2nd number : 24
The L.C.M. of 54 and 24 : 216
'''