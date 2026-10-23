
import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

sentences = [
    "The student reads a book in the library.",
    "A professor teaches the class.",
    "The students play on the ground.",
    "The clever boy uses a computer in the lab.",
    "The teacher explains the lesson to students."
]

grammar = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
    VP: {<MD>?<VB.*>+}
    PP: {<IN><NP>}
"""

chunker = nltk.RegexpParser(grammar)

for sentence in sentences:
    tokens = nltk.word_tokenize(sentence)
    tagged_words = nltk.pos_tag(tokens)
    tree = chunker.parse(tagged_words)

    print("\nSentence:", sentence)
    print("Chunk Tree:")
    print(tree)
