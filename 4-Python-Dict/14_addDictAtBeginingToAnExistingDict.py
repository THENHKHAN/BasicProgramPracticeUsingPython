# Python Program to Insertion at the beginning in OrderedDict

# We will learn how to write a program that will insert at the beginning in an OrderedDict using Python. For a given dictionary that is an OrderedDict, we have to insert items at the beginning of the dictionary.
'''
In an OrderedDict the order of the insertion of keys is maintained, unlike in a normal 
dictionary where the order of the keys is not saved.
'''
# Let us look at the sample input and output of the program.
'''
Input: original_dict = {1: 'a', 2: 'b', 3:'c'} item to be inserted (4, 'd')
Output: {4: 'd', 1: 'a', 2: 'b', 3: 'c'}
'''
# To execute this task we can use the following approaches:
'''
---> Using concatenation operator (+)
---> Using move_to_end() method of dict
'''


from collections import OrderedDict

def fun1(dct):
    # https://www.studytonight.com/python-programs/python-program-to-insertion-at-the-beginning-in-ordereddict
    pass

#  Using move_to_end() method
def usingMove2End(dct):
    ordDict = OrderedDict(dct)
    insrt = {"D": '400'}
    # dct.update(insrt) # by this we can add a new dictionary but at the end.Since in this normat dict there is no method called dict.move_to_end(). So in order to use ordDct.move_to_end() we need to convert normal dict to OrderDict.
    # print(dct) # {1: 'a', 2: 'b', 3: 'c', 'D': '400'}
    ordDict.update(insrt)
    # ordDict.move_to_end("D", last=False) # it is used to shift(start or end) the key-value based on the provided key
    ordDict.move_to_end(list(insrt.keys())[0], last=False) # dynamically geting key
    
    return dict(ordDict) # {'D': '400', 1: 'a', 2: 'b', 3: 'c'}
# The item which has to be inserted at the beginning is first added in the dictionary using update() then it is shifted to the beginning using the move_to_end() where the position is given as last=False.


myDict = {1: 'a', 2: 'b', 3:'c'} 
print(f"Original Dict : {myDict}" )
print("*********************   WAY : By using move_to_end() method ***********************")
print(f"after inserting at the begining : {usingMove2End(myDict)}")

#  I/O
'''
Original Dict : {1: 'a', 2: 'b', 3: 'c'}
*********************   WAY : By using move_to_end() method ***********************
after inserting at the begining : {'D': '400', 1: 'a', 2: 'b', 3: 'c'}
'''
