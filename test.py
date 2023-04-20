import matplotlib.pyplot as plt

import nltk
# Download the word corpus if it's not already installed
#nltk.download('words')

# Get the list of English words from the corpus
english_words = set(nltk.corpus.words.words())

# Create the array of arrays
words_array = [[] for _ in range(10)]
for word in english_words:
    length = len(word)
    if length >= 2 and length <= 11:
        inner_array = words_array[length-2]
        if len(inner_array) < 10:
            inner_array.append(word.lower())
        if len(inner_array) == 10:
            # Slice the array to limit it to 10 words
            words_array[length-2] = inner_array[:]

# Print the resulting array of arrays
for i, inner_array in enumerate(words_array):
    print(inner_array)