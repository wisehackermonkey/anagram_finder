# import itertools
# import pprint
# def generate_anagrams(word, limit=10000):
#     anagrams = set()
#     for perm in itertools.permutations(word):
#         if len(anagrams) >= limit:
#             break
#         anagrams.add(''.join(perm))
#     return list(anagrams)

# # Example usage
# word = "orancollins"
# limit = 10000
# anagrams = generate_anagrams(word, limit)
# anagrams= sorted(anagrams,reverse=True)
# print(len(anagrams))  # Should print 10000 or less
# pprint.pprint(anagrams[:100])  # Print first 10 anagrams to check


import nltk
from collections import defaultdict
from itertools import permutations

# Step 1: Preprocess words with NLTK
def preprocess_word(word):
    return ''.join(ch.lower() for ch in word if ch.isalpha())

# Step 2: Trie data structure
# Step 3: Build Trie from dictionary
def build_anagram_trie(dictionary):
    trie = Trie()
    for word in dictionary:
        processed_word = preprocess_word(word)
        sorted_word = ''.join(sorted(processed_word))
        trie.insert(sorted_word, word)
        # Also insert subsets of sorted_word to handle potential anagrams
        for i in range(1, len(sorted_word) + 1):
            for subset in permutations(sorted_word, i):
                subset_word = ''.join(subset)
                trie.insert(subset_word, word)
        
    return trie

# Step 4: Find anagrams using the Trie (for potential anagrams)
def find_anagrams(input_word, trie, limit=10000):
    processed_input = ''.join(sorted(preprocess_word(input_word)))
    potential_anagrams = trie.search(processed_input)
    
    if len(potential_anagrams) > limit:
        potential_anagrams = potential_anagrams[:limit]
    
    return potential_anagrams


# Example usage:
if __name__ == "__main__":
    nltk.download('words')
    input_word = "harplady"

    
    from nltk.corpus import words
    def remove_long_words(word_list, max_length):
        return [word for word in word_list if len(word) <= max_length]

    dictionary = set(remove_long_words(words.words(),len(input_word)))  # Get the NLTK dictionary
    anagram_trie = build_anagram_trie(dictionary)
    
    limit = 10000
    anagrams = find_anagrams(input_word, anagram_trie, limit)
    
    print(f"Potential Anagrams of '{input_word}' (limited to {limit} results):")
    for anagram in anagrams:
        print(anagram)
