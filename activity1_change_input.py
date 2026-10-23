import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

sentence = "The students read their textbooks."

tokens = nltk.word_tokenize(sentence)
tagged_words = nltk.pos_tag(tokens)

grammar = r"""
    NP: {<DT|PRP\$>?<JJ.*>*<NN.*>+}
    VP: {<MD>?<VB.*>+}
    PP: {<IN><NP>}
"""

chunker = nltk.RegexpParser(grammar)
tree = chunker.parse(tagged_words)

print("Input:", sentence)
print("\nPOS Tags:")
print(tagged_words)

print("\nChunk Tree:")
print(tree)