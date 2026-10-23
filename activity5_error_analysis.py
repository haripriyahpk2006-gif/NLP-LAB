
import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

sentence = "The scientist is developing a new application."

tokens = nltk.word_tokenize(sentence)
tagged_words = nltk.pos_tag(tokens)

original_grammar = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
    VP: {<MD>?<VB.*>+}
    PP: {<IN><NP>}
"""

original_chunker = nltk.RegexpParser(original_grammar)
original_tree = original_chunker.parse(tagged_words)

print("Original Chunk Tree:")
print(original_tree)

improved_grammar = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
    VP: {<VBZ|VBP|VBD><VBG>}
    VP: {<MD>?<VB.*>+}
    PP: {<IN><NP>}
"""

improved_chunker = nltk.RegexpParser(improved_grammar)
improved_tree = improved_chunker.parse(tagged_words)

print("\nImproved Chunk Tree:")
print(improved_tree)
