# Python Progam to Replace duplicate Occurrence in String
# LINK : https://www.studytonight.com/python-programs/python-progam-to-replace-duplicate-occurrence-in-string

'''
In this tutorial, you will learn to replace duplicate occurrences from a string. Occurrence is the **total number of times a word or a character 
has occurred in the string**.For a given string, 
we have to check if any word occurs more than once in the string and replace the duplicated word with a suitable word.

Let us look at the sample input and output of the program.

Input: "Python is good Python is easy"
Output: Python is good it is easy

To solve this problem in Python we can follow these approaches:
1- By using enumerate(), split() and loop
'''


# method-1 : Using enumerate(), split() and loop
def method1 (myStr, replace_word_collection):
    # 1st split :
    test_string_list = myStr.split(" ")
    r = set()
    print(f"List of words in the original string: {test_string_list}")
    for indx, ele in enumerate (test_string_list,0):
        # find which words going to replace
        if ele in replace_word_collection:
            if ele in r : # if second or more occurence only then we'll replace otherwise add in the r. Using index so that ordeering won't be disturb.
                     test_string_list[indx] = replace_word_collection[ele] # getting word that has to put in the original string
            else:
                 r.add(ele)
    else:
        #  now we need to make string again from list so we'll use join(iter)
        r = ' '.join(test_string_list) 
    # print(test_string_list) # ['Betty', 'is', 'a', 'girl.', 'She', 'is', 'good', 'in', 'Math', ',', 'that', 'is', 'her', 'favourite', 'subject.']

    return r

# the variable r is used as a set to keep track of the words that have already been replaced in the test_list. This is done to ensure that only the first occurrence of each word to be replaced
# If the current word (el) is in the replace_dict (i.e., it needs to be replaced), and if it's already in the set r, then it means that this is not the first occurrence of the word to be replaced.
 


# method-2 :  Using keys() + index() + list comprehension 
def method2 (myStr, replace_word_collection) :
     test_list = myStr.split(' ')
            # replace_word_collection.get(val) : replacing with the new value
     result = [replace_word_collection.get(value) if value in replace_word_collection.keys() and test_list.index(value) != indx  else value for indx, value in enumerate(test_list) ]
    #  print(result) # ['Gfg', 'is', 'best', '.', 'It', 'also', 'has', 'Classes', 'now.', 'They', 'help', 'understand', 'better', '.', '']
     return " ".join(result)

test_string = 'Betty is a girl. Betty is good in Math , Math is her favourite subject.'
print("\n **************  Method-1  *********************\n ")  
print("The original string is : " ,test_string)
replace_dict = {'Betty' :  'She', 'Math' : 'that' } # dictionary that will store the words and their replacement
replaced_word_string = method1(test_string, replace_dict )
print("The string after replacing : " , replaced_word_string) 


print("\n\n **************  Method-2  *********************\n")
# initializing string 
test_str = 'Gfg is best . Gfg also has Classes now. Classes help understand better . '
# printing original string 
print("The original string is : " , test_str) 
# initializing replace mapping 
repl_dict = {'Gfg' : 'It', 'Classes' : 'They' } 
replaced_word_string = method2(test_str, repl_dict )
print("The string after replacing : " , replaced_word_string) 




# INFO :

# lst.index(val) method returns the index of the given element in the list. 
'''
https://www.programiz.com/python-programming/methods/list/index

Note: The index() method only returns the first occurrence of the matching element.
'''
