import nltk
from nltk.corpus import brown
from nltk import UnigramTagger, BigramTagger

nltk.download('brown')
nltk.download('punkt')
nltk.download('punkt_tab')

# --------------------------------------------------
# PART A: Issues in PoS Tagging
# --------------------------------------------------

tagged_sentences = brown.tagged_sents(categories='news')

size = int(len(tagged_sentences) * 0.9)
train_data = tagged_sentences[:size]

unigram_tagger = UnigramTagger(train_data)
bigram_tagger = BigramTagger(
    train_data,
    backoff=unigram_tagger
)

# 1. Ambiguity
sentence1 = (
    "I saw her duck under the table and duck the flying ball."
)

print("\n1. AMBIGUITY")
print("Sentence:", sentence1)
print(bigram_tagger.tag(nltk.word_tokenize(sentence1)))

# 2. Unknown word
sentence2 = "Zorblax quickly entered the garden."

print("\n2. UNKNOWN WORD")
print("Sentence:", sentence2)
print(bigram_tagger.tag(nltk.word_tokenize(sentence2)))

# 3. Domain dependence
sentence3 = "OMG, this movie is soooo cool!"
sentence4 = "The moonlight dances softly on the sea."

print("\n3. DOMAIN DEPENDENCE")

print("Social media sentence:")
print(bigram_tagger.tag(nltk.word_tokenize(sentence3)))

print("\nPoem-like sentence:")
print(bigram_tagger.tag(nltk.word_tokenize(sentence4)))


# --------------------------------------------------
# PART B: HMM and Viterbi Algorithm
# --------------------------------------------------

states = ['DT', 'NN', 'VB']

start_p = {
    'DT': 0.6,
    'NN': 0.3,
    'VB': 0.1
}

trans_p = {
    'DT': {'DT': 0.05, 'NN': 0.85, 'VB': 0.10},
    'NN': {'DT': 0.10, 'NN': 0.30, 'VB': 0.60},
    'VB': {'DT': 0.40, 'NN': 0.50, 'VB': 0.10}
}

# Probabilities from the activity sheet
emit_p = {
    'DT': {'a': 0.5, 'the': 0.5},
    'NN': {'cat': 0.4, 'dog': 0.4, 'runs': 0.2},
    'VB': {'runs': 0.7, 'plays': 0.3}
}


def viterbi(obs, states, start_p, trans_p, emit_p):
    if not obs:
        return 0.0, []

    V = [{}]
    path = {}

    # Initialization
    for state in states:
        emission = emit_p[state].get(obs[0], 1e-6)
        V[0][state] = start_p[state] * emission
        path[state] = [state]

    print("\nInitialization:")
    for state in states:
        print(f"V[0][{state}] = {V[0][state]:.8f}")

    # Recursion
    for t in range(1, len(obs)):
        V.append({})
        new_path = {}

        for current in states:
            candidates = [
                (
                    V[t - 1][previous]
                    * trans_p[previous][current]
                    * emit_p[current].get(obs[t], 1e-6),
                    previous
                )
                for previous in states
            ]

            best_probability, best_previous = max(candidates)

            V[t][current] = best_probability
            new_path[current] = path[best_previous] + [current]

        path = new_path

        print(f"\nProbabilities for word '{obs[t]}':")
        for state in states:
            print(f"V[{t}][{state}] = {V[t][state]:.8f}")

    # Termination
    last_index = len(obs) - 1

    best_probability, best_state = max(
        (V[last_index][state], state)
        for state in states
    )

    return best_probability, path[best_state]


# Run Viterbi on the worksheet sentence
sentence = ['a', 'cat', 'runs']

probability, best_sequence = viterbi(
    sentence,
    states,
    start_p,
    trans_p,
    emit_p
)

print("\nVITERBI RESULT")
print("Sentence:", sentence)
print("Best Tag Sequence:", best_sequence)
print(f"Probability: {probability:.8f}")
