
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

def addk_prob(w1, w2, k):
    numerator = bigram_freq[(w1, w2)] + k
    denominator = unigram_freq[w1] + (k * vocab_size)
    return numerator / denominator

test_pairs = [
    ("i", "am"),
    ("am", "learning"),
    ("learning", "nlp"),
    ("natural", "language")
]

k_values = [0.01, 0.1, 0.5, 1.0]

print("Bigram\t\t", end="")
for k in k_values:
    print(f"k={k}\t\t", end="")
print()

for w1, w2 in test_pairs:
    print(f"{w1}->{w2}\t\t", end="")

    for k in k_values:
        probability = addk_prob(w1, w2, k)
        print(f"{probability:.5f}\t\t", end="")

    print()