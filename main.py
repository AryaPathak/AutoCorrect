import pandas as pd
import numpy as np
import textdistance
import re
from collections import Counter

#Storing all the words in a list

words = []

with open('sampleWordsBook.txt', 'r', encoding='utf-8') as f:
    file_name_data = f.read()
    file_name_data = file_name_data.lower()
    words = re.findall(r'\w+', file_name_data)
    
    
V = set(words)
#print(f"The first ten words are: \n{words[0:10]}")
#print(f"There are {len(V)} unique words")


#Finding frequency of words

word_freq_dict = {}
word_freq_dict = Counter(words)
#print(word_freq_dict.most_common()[0:10])


#Probability of occurance of each word

probs = {}
Total = sum(word_freq_dict.values())
for k in word_freq_dict.keys():
    probs[k] = word_freq_dict[k]/Total
    
    
#Sort similar words according to the Jaccard distance
#qval=2 means it compares every 2 letter section of word to compare words
#Jaccard tells how different two words are, that why (1 - Jaccard) to know how similar they are

def my_autocorrect(input_word):
    input_word = input_word.lower()

    if input_word in V:
        return('Your word to be correct')
    else:
        similarities = [1-(textdistance.Jaccard(qval=2).distance(v, input_word)) for v in word_freq_dict.keys()]
        df = pd.DataFrame.from_dict(probs, orient='index').reset_index()
        df = df.rename(columns={'index':'Word', 0:'Prob'})
        df['Similarity'] = similarities
        output = df.sort_values(['Similarity', 'Prob'], ascending=False).head()
        return(output)
    
print(my_autocorrect('neverteless'))