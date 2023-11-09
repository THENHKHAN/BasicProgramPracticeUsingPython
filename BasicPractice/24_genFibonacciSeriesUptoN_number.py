# Program to print Fibonacci series up to N  numbers
#INFO:
'''
It is a series in which any number in the series is the direct sum of previous two numbers in the series.
Following is Fibonacci Series -
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
More Mathematical terms
F(n) = F(n-1) + F(n-2)
Always, F(0) = 0, F(1) = 1
'''
#Method:
'''
Method Discussed
Method 1: Using Simple Iteration
Method 2: Using direct formulae
Method 3: Using Recursive Function            
Method 4: Using Dynamic Programming
NOTE: we'll be discussing remaining later
'''

# Method-1
def getFibonacciSeriesUptoNUsingLoop(n , n1 , n2) :  
    
    for it in range (0,n-2) :
        n3 = n1 + n2 
        print ( n3 , end= " ")
        n1 = n2
        n2 = n3 
# Method-2
def  getFibonacciUsingRecursion (num) :
    if (num <= 1):
        return num
    else:
        return ( getFibonacciUsingRecursion(num-1) + getFibonacciUsingRecursion (num-2) )

n = int(input("\n\n Enter how many sequence you want to genearte of FIBONACCI Series : "))
n1=0
n2 = n1+1 
print("\n***********   Using Method-1 Using iteration    ***************\n")
print(f"Fibonacci Series of total {n} number are: ")
print (f" {n1} {n2} " , end="" )
getFibonacciSeriesUptoNUsingLoop(n , n1 , n2 ) 

# using recursion
print("\n***********   Using Method-2 Using Recursion    ***************\n")
print (f" {n1} {n2} " , end="" )
for i in range(2 , n):
    print(getFibonacciUsingRecursion(i) , end=" ")
 