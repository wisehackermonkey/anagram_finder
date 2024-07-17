#%%
import nltk
from nltk.corpus import words
from collections import Counter
from pprint import pprint
# Download NLTK words if not already downloaded
nltk.download('words')

# # Load NLTK words list
word_list = words.words()
word_list = list(set(word.lower() for word in word_list))
print(word_list[:10])
#%%
# # Assume we only work with lowercase letters from 'a' to 'z'
# from collections import Counter
# from itertools import permutations
# #!/usr/local/bin/python3.5
# import itertools
# import sys
 
# __version__ = "1.1.0"


# def find_possible(lst):
#     """
#     Return all possible combinations of letters in lst

#     @type lst: [str]
#     @rtype: [str]
#     """
#     returned_list = []

#     for i in range(0, len(lst) + 1):
#         for subset in itertools.permutations(lst, i):
#             possible = ''
#             for letter in subset:
#                 possible += letter
#             if len(possible) == len(lst):
#                 # itertools.permutations returns smaller lists
#                 returned_list.append(possible)

#     return returned_list


# def return_words(lst, word_set):
#     """
#     Return combinations in that are words in word_set

#     @type lst: [str]
#     @type word_set: set(str)
#     @rtype: [str]
#     """
#     returned_list = []

#     for word in lst:
#         if word in word_set or word.capitalize() in word_set:
#             # Some words are capitalized in the word_set
#             returned_list.append(word)

#     return returned_list

#  #%%
# anagram_lst = []
# anagram = "triangle"
# for char in anagram:
#     anagram_lst.append(char)

# possible_words = find_possible(anagram_lst)
# actual_words = return_words(possible_words, nltk_words)

# print('Solutions:')
# if len(actual_words) == 0:
#     print('None found')
# else:
#     for item in set(actual_words):
#         # Running through in set form prevents duplicates
#         print(item)
# # %%
#%%
# Function to assign prime numbers to each letter
def prime_product(letter):
    primes = {
        'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17, 'h': 19,
        'i': 23, 'j': 29, 'k': 31, 'l': 37, 'm': 41, 'n': 43, 'o': 47, 'p': 53,
        'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79, 'w': 83, 'x': 89,
        'y': 97, 'z': 101
    }
    return primes.get(letter, 1)  # Return 1 for non-alphabet characters

# Function to compute prime product of a word
def compute_prime_product(word):
    product = 1
    for letter in word:
        product *= prime_product(letter.lower())
    return product

# Function to find anagrams using prime product approach
def find_anagrams(words):
    anagrams = {}
    for word in words:
        prime_prod = compute_prime_product(word)
        print(prime_prod)
        if prime_prod in anagrams:
            anagrams[prime_prod].append(word)
        else:
            anagrams[prime_prod] = [word]
    return [group for group in anagrams.values() if len(group) > 1]
#%%
# # Example usage:
word_list = word_list[:1000]
# word_list = ["listen", "silent", "enlist", "inlets", "banana", "nanaba"]
anagram_groups = find_anagrams(word_list)
print("Anagram groups found:")
for group in anagram_groups:
    print(group)

# %%
