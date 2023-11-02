
# Python Program to find HCF also called GCD:(gratest common factor/divisor)

#INFO:
'''
12-> 1,2,4,12 are factors
8-> 1,2,4,8 are the factors
==> so the common factors are : 1,2,4. But the greatest common factor  is : 4 hence 4 is the HCF/GCD of 8,12
'''


from math import gcd

# The gcd function was newly introduced in the Python version 3.9.0.
def getGCDByBuilt_inFun(n1,n2) :
        myGCD = gcd(n1,n2)  # buit-in function
        return myGCD


def getGCDbyLinearInteration(num1, num2) :
  minNum = min(num1,num2) # since GCD can be greater than the lowest number. EX- 13,26 => GCD = 13
  for myGcd in range(minNum , 0 , -1):
       if (num1 % myGcd == 0 and num2 % myGcd == 0) :
            return myGcd
       else:
            pass 
def lcmByGcd (num1 , num2 ) :
         myGcd = getGCDbyLinearInteration(num1, num2)
         myLcm = num1*num2 / myGcd
         return int(myLcm)

num1 = int (input("Please enter you 1st number : "))
num2 = int (input("Please enter you 2nd number : "))

print(f"The G.C.D. of {num1} and {num2} By Built-In: {getGCDByBuilt_inFun(num1, num2)}" )
print(f"The G.C.D. of {num1} and {num2} By Iteration-Logic: {getGCDbyLinearInteration(num1, num2)}" )
print(f"The L.C.M. of {num1} and {num2} By GCD-LCM relation: {lcmByGcd(num1, num2)}" )





# Relation b/w LCM and HCF : lets finding for n1 and n2 
'''
n1*n2 = lcm(n1,n2) * hcf(n1,n2)
'''

#INFO:
'''
The greatest common divisor (GCD) of two or more numbers is the greatest common factor number that divides them, exactly.
'''