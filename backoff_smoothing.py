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
alpha = 0.4

def stupid_backoff(w1, w2, w3):
    if trigram_freq[(w1, w2, w3)] > 0:
        probability = (
            trigram_freq[(w1, w2, w3)]
            / bigram_freq[(w1, w2)]
        )
        level = "trigram"


    elif bigram_freq[(w2, w3)] > 0:
        probability = alpha * (
            bigram_freq[(w2, w3)]
            / unigram_freq[w2]
        )
        level = "bigram"

    else:
        probability = (alpha ** 2) * (
            unigram_freq[w3] / N
        )
        level = "unigram"

    return probability, level

test_triples = [
    ("i", "am", "learning"),
    ("am", "learning", "nlp"),
    ("is", "fun", "to")
]

print("Alpha =", alpha)
print()

for w1, w2, w3 in test_triples:
    probability, level = stupid_backoff(w1, w2, w3)

    print(
        f"P({w3}|{w1},{w2}) "
        f"[Backoff -> {level}] = {probability:.5f}"
    )