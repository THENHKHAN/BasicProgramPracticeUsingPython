# Python Program to find Least Frequent Character in String
'''
you will learn to find the least frequent character in the string. Strings in Python are a sequence of characters wrapped inside single, double, or triple quotes. The frequency of a character is the total number of times that character occurs in the given string. We have to find and print the character which occurs the least in the string in our program.

Look at the examples to understand the input and output format.

Input: "apghphgg"
Output: a

Input: "hjkkjht"
Output: t

To execute this task we can follow multiple approaches, some are discussed below:

1---> By using keys in the dictionary and min() method
2---> By using Counter() and min() method

'''


from collections import Counter


# method-1 :
def byUsingGetFun(myStr):
    if len(myStr.replace(" ",""))<1: # also check if string have no character only space  so it will remove 
        print("string is empty ")
        return -1
    else:
        dictStoreFreq = {}
        for ele in myStr:
            dictStoreFreq[ele] = dictStoreFreq.get(ele, 0) +1
        
        print("Character with their Frequency : ", dictStoreFreq)
        minFreqCharacter = min(dictStoreFreq, key=dictStoreFreq.get)# it will iterate with values , whatever key'value will be minimum it will retunr that key.
        print("Here is the character which is minimum in string : ", minFreqCharacter) 
        return 1


#  method-1 using Counter class to frequency count of character
def byUsingCounterClass(myStr):
        if len(myStr.replace(" ",""))<1: # also check if string have no character only space  so it will remove 
            print("string is empty ")
            return -1
        else:
             charFreq = dict(Counter(myStr))
             print("Character with their Frequency : ", charFreq)
             minFreqChar = min(charFreq, key=charFreq.get)
             print("Here is the character which is minimum in string : ", minFreqChar) 
             return 1
             
             





InputStr =  "aaapghphghhhg"
print("my Input String:  " , InputStr)
print("******************* METHOD - 1 : By using Empty Dict, get function and min(iter,key)Function **********************************")
print(byUsingGetFun(InputStr))

print("******************* METHOD - 2 : By Counter Class of collections module and min() funciton **********************************")
print(byUsingCounterClass(InputStr))



# INPUT/ OUTPUT:

'''
my Input String:   aaapghphghhhg
******************* METHOD - 1 : By using Empty Dict, get function and min(iter,key)Function **********************************
Character with their Frequency :  {'a': 3, 'p': 2, 'g': 3, 'h': 5}
Here is the character which is minimum in string :  p
1
******************* METHOD - 2 : By Counter Class of collections module and min() funciton **********************************
Character with their Frequency :  {'a': 3, 'p': 2, 'g': 3, 'h': 5}
Here is the character which is minimum in string :  p
1

'''