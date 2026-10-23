
import nltk

# Download required resources
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

# Sample input
sentences = [
    "The teacher is in the lab.",
    "A clever student reads a paper.",
    "The students work in the library."
]

# Chunk grammar
grammar = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
    VP: {<MD>?<VB.*>+}
    PP: {<IN><NP>}
"""

chunker = nltk.RegexpParser(grammar)

for sentence in sentences:
    print("\nSentence:", sentence)

    # Tokenization and POS tagging
    tokens = nltk.word_tokenize(sentence)
    tagged_words = nltk.pos_tag(tokens)

    print("POS Tags:", tagged_words)

    # Chunk parsing
    chunk_tree = chunker.parse(tagged_words)

    print("Chunk Tree:")
    print(chunk_tree)
