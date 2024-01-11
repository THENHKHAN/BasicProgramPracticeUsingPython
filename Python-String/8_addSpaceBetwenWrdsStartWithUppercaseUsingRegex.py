# Python Program to put spaces between words starting with capital letters using Regex

'''
In this tutorial, we will learn to put space between words starting with capital letters. There is a set of words in a sentence and each word starts with an uppercase 
letter and there is no space between the words. So, we need to add space between each word. We will be using regex to do so.

Python Regex also called REs or regular expressions is a module using which we can specify rules to set the possible strings to match. 
It is available in re module.

Look at the examples to understand the input and output format.

Input: 'HelloWorldOfPython'
Output: Hello World Of Python

Input: 'LetUsStudyPython'
Output: Let Us Study Python

To add space between each word, we will use the following approach.
We will use re.findall() method to get the list of Words(Based on RegeX Pattern).

To extract the Words, use '[A-Z][a-z]*' expression. The following regular expression describes a word starting with an uppercase letter followed by multiple lowercase letters.
'[A-Z][a-z]*' ==> means Start with A to Z with capital and then zero or more a to z (small a to small z). * means 0 or more 
'''

import re

#input
string='HelloWorldOfPython'
# now we'll have to separate Words based on UPPER-CASE
words = re.findall('[A-Z][a-z]*', string)  # there is a 2nd arg which indicates which type of pattern will be matching.
print(words) # ['Hello', 'World', 'Of', 'Python'] noww nee to join and have space between each words
completeSent = " ".join(words)
print(completeSent) # Hello World Of Python 