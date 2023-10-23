
# Python Program to find max and min of three numbers


def maxMinFind(num1 , num2 , num3) :
    #  to find max among all three
    if (num1 > num2 and num1 > num3 ):
        print(f"{num1} is the Largest number among [{num1} , {num2} , {num3}]")
        #  to find min among b/w two
        if (num2>num3):
              print(f"{num3} is the Smallest number among [{num1} , {num2} , {num3}]")
        else:
             print(f"{num2} is the Smallest number among [{num1} , {num2} , {num3}]")
             

    elif ( num2 > num1 and num2 > num3 ):
        #  to find max among all three
        print(f"{num2} is the Largest number among [{num1} , {num2} , {num3}]")

        #  to find min among b/w two
        if (num1>num3):
              print(f"{num3} is the Smallest number among [{num1} , {num2} , {num3}]")
        else:
             print(f"{num1} is the Smallest number among [{num1} , {num2} , {num3}]")

    elif(num1 == num2 == num3) :
         print("ALL are equal")
    else:
            print(f"{num3} is the Largest number among [{num1} , {num2} , {num3}]")

            #  to find min among b/w two
            if (num2>num3):
                print(f"{num3} is the Smallest number among [{num1} , {num2} , {num3}]")
            else:
             print(f"{num2} is the Smallest number among [{num1} , {num2} , {num3}]")
            


num1 = int (input("Please enter you 1st number : "))
num2 = int (input("Please enter you 2nd number : "))
num3 = int (input("Please enter you 2nd number : "))

maxMinFind(num1 , num2 , num3)

# More optimize and simple

'''
 # Initialize max_num and min_num with the first number
    max_num = num1
    min_num = num1

    # Find the maximum and minimum values
    if num2 > max_num:
        max_num = num2
    if num3 > max_num:
        max_num = num3

    if num2 < min_num:
        min_num = num2
    if num3 < min_num:
        min_num = num3

    # Print the results
    print(f"{max_num} is the Largest number among [{num1}, {num2}, {num3}]")
    print(f"{min_num} is the Smallest number among [{num1}, {num2}, {num3}]")

    if num1 == num2 == num3:
        print("All numbers are equal")
'''
# or we can improve the already written logic : 
'''
Means we can define two more variable and initialize them with any of the number and according to condition we can update them.
And we have written many times print statement  so we can write one print statement according to recent updated two more variable
value.
'''