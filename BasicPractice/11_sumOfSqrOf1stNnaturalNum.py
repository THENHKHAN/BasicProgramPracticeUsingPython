
# Python Program to Calculate the Sum of Squares of First n Natural Number
# 1² + 2² + 3² + 4².....+ N²
# Two way to dot it . 1) through formula -(n*(n+1)*(2n+1))/6 and 2) using loop

def sufOfSqrOfFirstNNaturalNum( n ) :
    # we'll be using loop to get the sum of square till n
     sum = 0 
     for num in range(1,n+1) :
          sum += num**2
    
     return sum


n = int(input("Enter the value of n: "))
print(f"Sum of Square of 1st {n} natural number : {sufOfSqrOfFirstNNaturalNum(n)}")

# I/O
'''
Enter the value of n: 20
Sum of Square of 1st 20 natural number : 2870
'''