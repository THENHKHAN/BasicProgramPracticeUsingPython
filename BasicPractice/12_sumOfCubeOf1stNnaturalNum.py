# Python Program to find Cube Sum of First n Natural Numbers
# 1³ + 2³ + 3³ + 4³.....+ N³
#  Two way to dot it . 1) through formula -(n*(n+1)/2)**2 and 2) using loop

def sufOfCubeOfFirstNNaturalNum( n ) :
    # we'll be using loop to get the sum of square till n
     cube = 0

     for num in range (1,n+1) :
          print(cube)
          cube += num**3
    
     return cube


n = int(input("Enter the value of n: "))
print(f"Sum of CUBE of 1st {n} natural number : {sufOfCubeOfFirstNNaturalNum(n)}")

# I/O
'''
Enter the value of n: 4
Sum of CUBE of 1st 4 natural number : 100
'''