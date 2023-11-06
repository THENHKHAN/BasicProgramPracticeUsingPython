
# Check if a Year is a Leap Year or Not in Python
'''
Conditions for a Leap Year:
Here are the two conditions that any year must satisfy to be called a leap year-

1--> The year must be perfectly divisible by 400. for centuary year. whose yr is end with double zero.
2--> The number must be divisible by 4 but not by 100.

'''

def checkLeapYr (year):
    if ( (year % 400 == 0) or (year%4==0 and year%100 != 0) ): # ex-1700 is not a leap yr and 2000 is bcz one is exactly divisible by 400 and other not
        return True
    else:
        return False

yr = int (input("Please enter your year: "))
check = checkLeapYr(yr)
if(check):
    print(f"YES, {yr} is a leap year")
else:
    print(f"NO, {yr} is a leap year")