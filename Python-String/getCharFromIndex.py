
# Get the character of a string at kth position where k start from 1 

myStr = input("please enter your string : ")
print (f"Choose the position of character you want. But must be between 1 to {len(myStr)}:" , end=" ")
pos = int(input())

# multiline is also called docString in python
print(f'''
    String character at Position  {pos} is : {myStr[pos-1]} 
''')

## OUTPUT
'''
please enter your string : abcdefgh
Choose the position of character you want. But must be between 1 to 8: 5

    String character at Position  5 is : e

'''