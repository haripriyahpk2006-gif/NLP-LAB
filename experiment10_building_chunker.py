
import nltk

# Download required resources
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

# Sample input
sentence = "The intelligent student reads a book in the library."

# Step 1: Tokenization
tokens = nltk.word_tokenize(sentence)

# Step 2: POS tagging
tagged_words = nltk.pos_tag(tokens)

print("Input Sentence:")
print(sentence)

print("\nPOS-tagged words:")
print(tagged_words)

# Step 3: Define chunk grammar
grammar = r"""
    NP: {<DT>?<JJ.*>*<NN.*>+}
    VP: {<MD>?<VB.*>+}
    PP: {<IN><NP>}
"""

# Step 4: Create the chunker
chunker = nltk.RegexpParser(grammar)

# Step 5: Parse the tagged words
chunk_tree = chunker.parse(tagged_words)

print("\nChunk Tree:")
print(chunk_tree)

