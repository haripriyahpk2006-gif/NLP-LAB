
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')

from nltk import bigrams, FreqDist
from nltk.tokenize import word_tokenize

corpus = """I am learning natural language processing.
I am learning smoothing techniques for NLP.
Natural language processing is fun to learn."""

tokens = word_tokenize(corpus.lower())

unigram_freq = FreqDist(tokens)
bigram_freq = FreqDist(bigrams(tokens))
vocab_size = len(unigram_freq)

def add1_prob(w1, w2):
    numerator = bigram_freq[(w1, w2)] + 1
    denominator = unigram_freq[w1] + vocab_size
    return numerator / denominator

test_pairs = [
    ("i", "am"),
    ("am", "learning"),
    ("learning", "nlp"),
    ("natural", "language")
]

print("Vocabulary size (V):", vocab_size)
print("\nBigram\t\tCount\tAdd-1 Probability")

for w1, w2 in test_pairs:
    count = bigram_freq[(w1, w2)]
    probability = add1_prob(w1, w2)

    print(f"{w1} -> {w2}\t{count}\t{probability:.5f}")
