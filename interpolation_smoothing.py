
# Experiment 3: Linear Interpolation Smoothing

import nltk
nltk.download('punkt')
nltk.download('punkt_tab')

from nltk import bigrams, trigrams, FreqDist
from nltk.tokenize import word_tokenize

corpus = """I am learning natural language processing.
I am learning smoothing techniques for NLP.
Natural language processing is fun to learn."""

tokens = word_tokenize(corpus.lower())

unigram_freq = FreqDist(tokens)
bigram_freq = FreqDist(bigrams(tokens))
trigram_freq = FreqDist(trigrams(tokens))

N = len(tokens)

# Weights must sum to 1
lambda1 = 0.1
lambda2 = 0.3
lambda3 = 0.6

def interpolated_prob(w1, w2, w3):
    # Unigram probability
    p_uni = unigram_freq[w3] / N

    # Bigram probability
    if unigram_freq[w2] > 0:
        p_bi = bigram_freq[(w2, w3)] / unigram_freq[w2]
    else:
        p_bi = 0

    # Trigram probability
    if bigram_freq[(w1, w2)] > 0:
        p_tri = (
            trigram_freq[(w1, w2, w3)]
            / bigram_freq[(w1, w2)]
        )
    else:
        p_tri = 0

    return (
        lambda1 * p_uni
        + lambda2 * p_bi
        + lambda3 * p_tri
    )

test_triples = [
    ("i", "am", "learning"),
    ("am", "learning", "nlp"),
    ("is", "fun", "to")
]

print("Interpolation weights:")
print("Lambda1 =", lambda1)
print("Lambda2 =", lambda2)
print("Lambda3 =", lambda3)
print()

for w1, w2, w3 in test_triples:
    probability = interpolated_prob(w1, w2, w3)

    print(
        f"P({w3}|{w1},{w2}) = {probability:.5f}"
    )