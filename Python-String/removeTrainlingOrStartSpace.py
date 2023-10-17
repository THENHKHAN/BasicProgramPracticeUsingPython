
# Remove whiteSpace at the beggining or at the end (end also called trailing)



def stripLeadingAndTrailSpaces(orginalStr) :
    # prints the string without stripping 
        print("orginalStr: " , orginalStr)  
        
        # prints the string by removing leading and trailing whitespaces 
        print("stripped white space of Original : " ,orginalStr.strip())    
        
        # prints the string by removing geeks 
        print("stripped * geeks* of Original : "  , orginalStr.strip(" geeks"))


def stripSpecificChar(str) :
    stripped_string =  str.strip("Nooan")
    print(f"Original String : {str}")
    print(f"AFter Stripped : {stripped_string}")
   
def stripNewLineChar(orgStr):
    print("****** Strip new Line Character   ******")
    stripped_string =  orgStr.strip()
    print(f"Original String : {orgStr}") # string will print in new line since in string new line char is already there
    print(f"AFter Stripped : {stripped_string}") # this will not since removed



myStr = input("please enter your string : ")
# there is a strip function
stripped_string = myStr.strip() # it returned a copy of the stripped strings. and does not affect the original string
print(f"AFter Stripped : {stripped_string}")
print(f"Original String : {myStr}")

#  Stripping String with Strip() function
stripLeadingAndTrailSpaces("""    geeks for geeks    """ )

#  Stripping Specific Character with Strip() Function : to remove a specific set of characters from a string.

stripSpecificChar("Noorul Huda Khan")


#  Removing NewLine using Strip() Function

stripNewLineChar("\nHello, World!\n")


# OUTPUT
'''
please enter your string :                   thhh
AFter Stripped : thhh
Original String :                   thhh
orginalStr:      geeks for geeks
stripped white space of Original :  geeks for geeks
stripped * geeks* of Original :  for
Original String : Noorul Huda Khan
AFter Stripped : rul Huda Kh
****** Strip new Line Character   ******
Original String :
Hello, World!

AFter Stripped : Hello, World!

'''


# Some INFO :
'''
strip() is an inbuilt function in the Python programming language that returns a copy of the string with both 
                                leading and trailing characters removed (based on the string argument passed).
                    
Syntax: string.strip([chars])

Parameter: There is only one optional parameter in it. chars – a string specifying the set of characters to be removed. If the optional chars parameter is not given, all leading and trailing whitespaces are removed from the string.

Return Value: Returns a copy of the string with both leading and trailing characters removed.                

PURPOSE : When a developer wishes to remove characters or whitespaces from the beginning or end of a string,

Closer LOOK:
 Let's take a closer look at it: 

- The strip() function assists in removing characters from the beginning or end of a string for characters supplied as arguments to the strip() function ().
- If the string has no whitespaces and the characters argument is not supplied, the string is returned as is.
- It is also beneficial to eliminate whitespaces from the beginning and end of the text.
- If the string contains whitespaces and no character arguments are supplied, the string will be returned after discretizing the whitespaces.

IMP-Warining: The strip() method in Python removes specified characters from the leading (beginning) and trailing (end) positions of the string. It doesn't remove occurrences 
                of those characters that are within the string. 

'''
