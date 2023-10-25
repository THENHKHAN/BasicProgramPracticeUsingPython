
# The split() method splits a string into a list.You can specify the separator, default separator is any whitespace.


def splitDefault (myStr) :
    lstOfString = myStr.split(" ")
    print(lstOfString)

def splitBasedOnDelimeter(myStr , delimeter) :
    lstOfString = myStr.split(delimeter)
    print(lstOfString)


def splitBasedOnDelimeterAndMaxSplit (myStr , delimeter , maxSplit ) :
      lstOfString = myStr.split(delimeter , maxSplit)
      print(lstOfString)



txt = "welcome to the jungle"
print ("********   Default splitting       ***********")
splitDefault(txt)
print ("********   based on provided delimeter splitting       ***********")

str1 = "hello, my name is Peter, I am 26 years old"
splitBasedOnDelimeter(str1 , "," )
# Use a hash character as a separator:
str2 = "apple#banana#cherry#orange"
splitBasedOnDelimeter(str2 , "#" )

# Split the string into a list with max 2 items:
str3  = "apple#banana#cherry#orange"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
splitBasedOnDelimeterAndMaxSplit(str3 , "#"  , 1)

# OUTPUT

'''

********   Default splitting       ***********
['welcome', 'to', 'the', 'jungle']
********   based on provided delimeter splitting       ***********
['hello', ' my name is Peter', ' I am 26 years old']
['apple', 'banana', 'cherry', 'orange']
['apple', 'banana#cherry#orange']


'''
# SyntaX :
'''
--> The split() method splits a string into a list.

--> You can specify the separator, default separator is any whitespace.

Note: When maxsplit is specified, the list will contain the specified number of elements plus one.

--> string.split(separator, maxsplit) -maxsplit is optional
'''