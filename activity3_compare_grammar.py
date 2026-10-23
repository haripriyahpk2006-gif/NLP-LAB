
import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

sentence = "The student reads a book in the library."

tokens = nltk.word_tokenize(sentence)
tagged_words = nltk.pos_tag(tokens)


np_grammar = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
"""

np_chunker = nltk.RegexpParser(np_grammar)
np_tree = np_chunker.parse(tagged_words)

print("NP Only Grammar:")
print(np_tree)

full_grammar = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
    VP: {<MD>?<VB.*>+}
    PP: {<IN><NP>}
"""

full_chunker = nltk.RegexpParser(full_grammar)
full_tree = full_chunker.parse(tagged_words)

print("\nNP + VP + PP Grammar:")
print(full_tree)
