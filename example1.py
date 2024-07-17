
#%%
import nltk
nltk.download('words')
from nltk.corpus import words

list(words.words())[:100]
# %%
def remove_long_words(word_list, max_length):
    return [word for word in word_list if len(word) <= max_length]

word_list = words.words()# ["apple", "banana", "grape", "pineapple", "orange"]
max_length = 6

filtered_words = remove_long_words(word_list, max_length)
print(filtered_words)  # Output: ['apple', 'banana', 'grape', 'orange']
len(filtered_words)
# %%
def bucket_strings_by_length(strings):
    buckets = {}
    for string in strings:
        length = len(string)
        if length not in buckets:
            buckets[length] = []
        buckets[length].append(string)
    return buckets

# Example usage:
big_array = ["apple", "banana", "cat", "dog", "elephant", "fox", "giraffe", "hat", "ice", "jaguar", "kite", "lion", "monkey", "newt", "owl"]
buckets = bucket_strings_by_length(big_array)

for length, bucket in buckets.items():
    print(f"Bucket {length}: {bucket}")

# %%
def bucket_strings_by_length(strings):
    # Initialize 15 buckets for lengths 1 to 15
    buckets = [[] for _ in range(15)]

    # Iterate through each string in the input array
    for s in strings:
        length = len(s)
        if 1 <= length <= 15:  # Only consider lengths 1 to 15
            buckets[length - 1].append(s)  # Append the string to the corresponding bucket

    return buckets

# Example usage:
big_array = ["a", "apple", "ball", "cat", "dog", "elephant", "fish", "go", "hat", "ice", "jump", "kite", "lion", "moon", "net", "owl", "pie", "queen", "rat", "sun", "tree", "umbrella", "violet", "water", "x-ray", "yarn", "zebra"]
buckets = bucket_strings_by_length(big_array)
def bucket_print(buckets):
# Print out the buckets
    for i, bucket in enumerate(buckets):
        print(f"Bucket {i + 1}: {bucket}")
bucket_print(buckets)
# %%
