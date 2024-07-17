#%%
import nltk
from nltk.corpus import words

# Download the words corpus if not already downloaded
nltk.download('words')

# Load the English words corpus
word_list = words.words()
word_list = list(set(word.lower() for word in word_list))

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
def find_anagrams(word_list):
    anagrams = {}
    for word in word_list:
        prime_prod = compute_prime_product(word)
        if prime_prod in anagrams:
            anagrams[prime_prod].append(word)
        else:
            anagrams[prime_prod] = [word]
    return [group for group in anagrams.values() if len(group) > 1]

# Example usage:
anagram_groups = find_anagrams(word_list)
print("Anagram groups found:")
#%%
anagram_groups = sorted(anagram_groups)
for group in anagram_groups:
    print(group)


# %%
