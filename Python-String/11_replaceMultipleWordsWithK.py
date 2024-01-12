# Python Program To Replace multiple words with K
'''
A word is a substring. For a given string, we have to replace multiple words in the string with a single letter k. multiple words could be same or different.

EX: 'Studytonight has best tutorials in python'
multiple words need to replace  - best, tutorials,  python
OUTPUT : Studytonight has k k in k
'''
# intiution - we have to make a list words  that  that needs to be replace by K in the give string:
# APPROCAH: - we need to split and check for with word_list and then replac with K


def usingSplitAndJoin(myTestingStr, word_list, replacedWord):
    listOfWordsInGivenString = myTestingStr.split() # bydefault it willl split n the basis of " " white space - give list of words
    # print(listOfWordsInGivenString) # ['Studytonight', 'has', 'best', 'tutorials', 'in', 'python']
    storReplaceWordList = []
    for StrWord in listOfWordsInGivenString:
        if StrWord in word_list:
            storReplaceWordList.append(StrWord.replace(StrWord, "K")) # replacing that word by K

        else: # like this  has its not there in word_list so it will beappend in else block 
            storReplaceWordList.append(StrWord)

    replaced_string = " ".join(storReplaceWordList)        
    print("After replacing word by K : ", replaced_string)


def usingJoinSplitListCimprhension(myTestingStr, word_list, replacedWord) :
    # we;ll create list like above storReplaceWordList = [] by LIST comprehension
    replced_wrodsList = [replacedWord if StrWord in word_list else StrWord for StrWord in myTestingStr.split() ]
    # print(replced_wrodsList) # ['Studytonight', 'has', 'K', 'K', 'in', 'K'] NOW WEED to make string from list SO we'll use JOIN
    replaced_string = " ".join(replced_wrodsList)
    print("After replacing word by K : ", replaced_string)


myTestingStr = 'Studytonight has best tutorials in python'
print("\n ### ORIGIANAL STRING : " , myTestingStr)
word_list = ["best", "tutorials", "python"] #these must be present in the given string if want to replace bcz we'll have to checkc then replace
replacedWord = "K"
print(f"\n New String After replacing these words {word_list} in the above string\n ")


print("**************    METHOD-1 By  usingSplitAndJoin  **************************** ")
usingSplitAndJoin(myTestingStr, word_list, replacedWord)

print("\n")

print("**************    METHOD-2 By  usingSplitAndJoin  **************************** ")
usingJoinSplitListCimprhension(myTestingStr, word_list, replacedWord)

# join(), split() and list comprehension :
'''

In this approach, we will first declare a list with words that have to be replaced and then traverse to that words in the string and replace it with the letter k.
The join() method is used to join list elements together. It will return a string after joining the words in the list.
The split() method will be used to get words from the string.
We will use list comprehension, which is a shorter syntax for creating a new list based on the values of an existing list.
'''

# INPUT/OUTPUT :

'''
 ### ORIGIANAL STRING :  Studytonight has best tutorials in python

 New String After replacing these words ['best', 'tutorials', 'python'] in the above string

**************    METHOD-1 By  usingSplitAndJoin  ****************************
After replacing word by K :  Studytonight has K K in K


**************    METHOD-2 By  usingSplitAndJoin  ****************************
After replacing word by K :  Studytonight has K K in K
'''