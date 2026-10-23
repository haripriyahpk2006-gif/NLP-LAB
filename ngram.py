
import nltk

nltk.download('punkt')
nltk.download('punkt_tab')

from nltk import bigrams, trigrams, FreqDist
from nltk.tokenize import word_tokenize

corpus = """I am learning natural language processing.
I am learning smoothing techniques for NLP.
Natural language processing is fun to learn."""

tokens = word_tokenize(corpus.lower())

print("Tokens:", tokens)
print("Total tokens:", len(tokens))