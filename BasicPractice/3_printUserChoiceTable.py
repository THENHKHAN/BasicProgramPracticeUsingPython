#  we'll be printing user define table in  a table format

userIn = int (input ("please enter your number to get the table of: "))
print(f"\nTable of {userIn} : \n")
for fact in range(1,10+1):
    print (f"{userIn} X {fact} = {userIn * fact}")


# OUTPUT:
'''
please enter your number to get the table of: 11

Table of 11 :

11 X 1 = 11
11 X 2 = 22
11 X 3 = 33
11 X 4 = 44
11 X 5 = 55
11 X 6 = 66
11 X 7 = 77
11 X 8 = 88
11 X 9 = 99
11 X 10 = 110


'''