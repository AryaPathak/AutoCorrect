With the context of machine learning, autocorrect is based on natural language processing. As the name suggests it is programmed to correct spellings and errors while typing

To run the autocorrect

Download the files and run the file main.py

In last line of main.py, put the word you want to check

print(my_autocorrect('___YOUR_WORD___'))

To extext the vocabulary change or add more text in the sampleWordsBook.txt file




How the word comparison works ? 

Jaccard Similarity is a measure of how similar two sets are. In this case, the sets are sequences of character n-grams.
qval=2 means that we are using bigrams (sequences of 2 characters) to compare the words. This means the string is broken down into overlapping groups of 2 characters. For example:
For the word "test", the bigrams would be: ["te", "es", "st"].
For "neverteless", the bigrams would be: ["ne", "ev", "ve", "er", "rt", "te", "el", "le", "es", "ss"].



Since textdistance.Jaccard().distance() returns a distance value (how different two words are), the formula 1 - distance gives us the similarity value.
If the distance is 0 (words are identical), the similarity will be 1.
If the distance is 1 (words are completely different), the similarity will be 0.
