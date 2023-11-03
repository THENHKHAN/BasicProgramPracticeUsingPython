

# Using Lambda Function with List Comprehension
'''
In this instance, we will apply the lambda function combined with list comprehension and the lambda keyword with a for loop.
Using the Lambda Function with List Comprehension, we can print the square value from 0 to 10.
For printing the square value from 0 to 10, we create a loop range from 0 to 11.
'''

# Question: Calculate square of each number of lists using list comprehension.There no list is given so we need to make everything by ourself.


print("\n\n ******************  Using list compreshension & lambda in different line and with map function. **********************\n")

#way-1 : generate the list. Can be easily generated using list comprehension
myList = [num for num in range(0 , 10+1)] # list comprehension
sqrList = lambda num : num**2
print(f" Origin Generated LIST : {myList}")
map_it = map(sqrList,myList)
print(f"The square value of all numbers from 0 to 10: {list(map_it)}")


print("\n\n ******************  Using list compreshension & lambda in same line and withOUT map function. **********************\n")

# Other way : using list comprehension along with lamda
myListCompre = [lambda num = ele : num**2 for ele in range(0,10+1)] # list generated and along the way square made. BUT IMP
# myListCompre is not a list of square number . It is a list of lambda function. It is similar to making function without def keyword means only with lambda like ==>  y = lambda num : num+num . and calling y() so y work as a function.
print(f'The square value of all numbers from 0 to 10: {myListCompre}\n')
# result = [y() for y in myListCompre]  -- one way to resolve from lambda
# print(result)
'''Other way - using for loop and calling each time myListCompre as function'''
print("The square value of all numbers from 0 to 10: " , end= " ")
for sqr in myListCompre : # now here sqr will work as function like we have explained above as y.
    print(sqr(), end=" ")


# INPUT/OUTPUT
'''

 ******************  Using list compreshension & lambda in different line and with map function. **********************

 Origin Generated LIST : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
The square value of all numbers from 0 to 10: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


 ******************  Using list compreshension & lambda in same line and withOUT map function. **********************

The square value of all numbers from 0 to 10: [<function <listcomp>.<lambda> at 0x0000025E2DCFECB0>, <function <listcomp>.<lambda> at 0x0000025E2DCFEE60>, <function <listcomp>.<lambda> at 0x0000025E2DCFF010>, <function <listcomp>.<lambda> at 0x0000025E2DCFF1C0>, <function <listcomp>.<lambda> at 0x0000025E2DCFF250>, <function <listcomp>.<lambda> at 0x0000025E2DCFF2E0>, <function <listcomp>.<lambda> at 0x0000025E2DCFF370>, <function 
<listcomp>.<lambda> at 0x0000025E2DCFF400>, <function <listcomp>.<lambda> at 0x0000025E2DCFF490>, <function <listcomp>.<lambda> at 0x0000025E2DCFF520>, <function <listcomp>.<lambda> at 0x0000025E2DCFF5B0>]


'''

