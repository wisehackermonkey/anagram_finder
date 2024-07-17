#%% 
def bucket_print(buckets):
    # Print out the buckets
    for i, bucket in enumerate(buckets):
        print(f"Bucket {i + 1}: {len(bucket)}, {bucket[:100]}...")
def bucket_strings_by_length(strings):
    # Initialize 15 buckets for lengths 1 to 15
    buckets = [[] for _ in range(15)]

    # Iterate through each string in the input array
    for s in strings:
        length = len(s)
        if 1 <= length <= 15:  # Only consider lengths 1 to 15
            buckets[length - 1].append(s)  # Append the string to the corresponding bucket

    return buckets 
import nltk
from nltk.metrics import edit_distance, jaccard_distance
import textdistance

def sort_words_by_levenshtein(words, target_word):
    words = set(words)
    # Calculate Levenshtein distance for each word in the list
    distances = [(word, textdistance.damerau_levenshtein.distance(word, target_word)) for word in words]
    
    # Sort words based on Levenshtein distance
    sorted_words = sorted(distances, key=lambda x: x[1])
    
    # Return sorted words
    return [word[0] for word in sorted_words],distances
import itertools


def generate_anagrams(s):
    n = len(s)
    result = []
    
    def heap_permutation(n, A):
        if n == 1:
            result.append(''.join(A))
            return
        
        for i in range(n):
            heap_permutation(n - 1, A)
            
            # if n is odd, swap first and last element
            # if n is even, swap ith and last element
            if n % 2 == 0:
                A[i], A[n - 1] = A[n - 1], A[i]
            else:
                A[0], A[n - 1] = A[n - 1], A[0]
    
    heap_permutation(n, list(s))
    return result



#%% main
import nltk
from pprint import pprint
nltk.download('words')
from nltk.corpus import words
# normalized
words_list = [word.lower() for word in words.words()]
#%%
"reveals" in words_list
#%%
buckets = bucket_strings_by_length(words_list)
#%%
buckets[0] = ["a", "i", "u"]
bucket_print(buckets[:14])
# %%
input_word = "appleorange"

fours = buckets[5]

matches,distances = sort_words_by_levenshtein(fours,input_word)
pprint(matches)
# %%
def filter_array_starts_with(arr, start_words):
    return [item for item in arr if any(item.startswith(word) for word in start_words)]
# arr = ["apple", "banana", "orange", "kiwi", "pear"] ##perms
# input_word = "listen"
input_word = "several"
# input_word = "listen"
# bucket_print(buckets)
perm_list = generate_anagrams(input_word)
# print( perm_list)
print(len(perm_list))
# perm_list = sorted(perm_list)
input_length = len(input_word)-1
 
common_matches = set(buckets[0]+buckets[1]+buckets[2]+buckets[3]+buckets[4]+buckets[5]+buckets[6]+buckets[7]+buckets[8])
len(common_matches)
output = []
for perm in perm_list:
    if perm in common_matches:
        output += [perm]
    print(f". {perm }")
print(output)
# %%
