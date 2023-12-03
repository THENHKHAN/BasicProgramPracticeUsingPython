# Print anagrams together in Python using List and Dictionary. And if already todegther then leave as it is.
"""
We will learn to find and print anagrams in a dictionary using list and dictionary concepts in Python. 
Anagrams are words that are formed by arranging the same letters in different orders. For example, cat and act are anagrams 
because they have the same characters which are just arranged differently. """
'''
Take a look at the sample input-output format.

Input: ['care', 'knee', 'race', 'keen']
Output: ['care', 'race', 'knee', 'keen']

Input: ['care', 'knee', 'race', 'keen']
Output: ['care', 'race', 'knee', 'keen']
'''


def printTogetherAnagrams(word_list):
    # Create an empty dictionary to store anagrams
    anagram_dict = {}

    # Iterate through each word in the list
    for word in word_list:
        # Convert the word into a sorted tuple of characters
        sorted_chars = tuple(sorted(word))

        # Check if the sorted characters tuple is already in the dictionary
        if sorted_chars in anagram_dict:
            # If it is, add the current word to the list of anagrams
            anagram_dict[sorted_chars].append(word)
            
        else:
            # If it's not, create a new list with the current word
            anagram_dict[sorted_chars] = [word]

    # Create a list to store the final result
    result_list = []

    # Iterate through the values in the dictionary (lists of anagrams)
    for anagrams in anagram_dict.values():
        # Extend the result list with the list of anagrams
        result_list.extend(anagrams)

    return result_list

# Example usage:
input_words = ['care', 'knee', 'race', 'keen']
groupAnagrams = printTogetherAnagrams(input_words)

# Print the result
print(groupAnagrams)



# APPROACH:
'''
The approach to solving this problem is to first traverse the list containing strings of words and sort each string in ascending 
order using the sorted() method. Then we will set the sorted value as the key and the original value as the value in the key.

Then we will check if the key is present or not in the dictionary. Set an empty list to the key and add value to it, 
if the key is already present then we will simply append the value.

Now each key will be containing a list of strings that are anagram together.
'''