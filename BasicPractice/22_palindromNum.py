
# Check Whether or Not the Number is a Palindrome in Python

#INFO:
'''
Palindromic Numbers:
The Numbers that when reversed is the same as the original number itself are known as Palindromic Numbers.
'''
# ways:
'''
For a number to be a Palindrome, the number must be the same when reversed. If the number doesn’t match the reverse of itself, the number is not a Palindrome.

Method 1:  Using Simple Iteration.
Method 2: Using String Slicing.
Method 3: Using Recursion
Method 4:  Using Character matching
Method 5: Using Character matching updated
Method 6: Using Built-in reversed function
Method 7:  Building reverse one char at a time
Method 8: Using Flag and backward reading
Method 9: Bonus using backward slicing

------->>>> But right now - 06Nov/2023 will be dicussing only 1 or 2 methods:
'''


def isPanlindromNumberByRvrNum (num):
     getRvrNum = 0
     tempNum = num
     while(num > 0) :
          rem = num % 10
          getRvrNum = getRvrNum * 10 + rem
          num //= 10
     else:
        return True if (getRvrNum == tempNum)  else  False


# Using Character matching- 2
def isPanlindromNumberByCharMatch (myNum) :
    makeNumAsStr = str(myNum)
    mid = len(makeNumAsStr) // 2
    for ind in range(0,mid):
        if(makeNumAsStr[ind]!=makeNumAsStr[len(makeNumAsStr)-1-ind]):# comparing starting character with from the ending
            return False
    else: # it will execute after successfully run for loop
            return True    
    


n = int(input("\n\n Enter the number you want to check Palindrome number: "))
print("\n***********   Using Method-1 Revrsing the number    ***************\n")
print(f"YES, {n}  is a Palindrome number") if isPanlindromNumberByRvrNum(n)  else print(f"NO, {n} is NOT a Palindrome number") 


print("\n***********   Using Method-2 checking each character    ***************\n")
print(f"YES, {n}  is a Palindrome number") if isPanlindromNumberByCharMatch(n)  else print(f"NO, {n} is NOT a Palindrome number") 
