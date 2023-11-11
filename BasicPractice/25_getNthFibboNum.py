
# Find nth fibonacci number : Assuming fibonacci are 0 1 1 2 3 5  8 13 ...........
                        # 0th 1st 2nd 3rd  - 0 1 1 3 ...etc
'''Mean starting from 0 '''

# Using recursion

def getNthFibo (num ) :

    # base condition :
    if (num < 2 ) :
        return num # less than 2 number will return number
    return ( getNthFibo(num-1) + getNthFibo(num-2) )

n = int (input("please enter which nth Fibonacci number you want: "))
print(f"You {n}th Fibonacci number is :  {getNthFibo(n)}" )