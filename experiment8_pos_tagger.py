
import nltk

# Download required resources (run once)
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

# Sample input
sentence = "The intelligent student reads a book."

# Tokenization
tokens = nltk.word_tokenize(sentence)

# POS tagging
tagged_words = nltk.pos_tag(tokens)

# Display output
print("Input sentence:", sentence)
print("\nWord\t\tPOS Tag")
print("-" * 25)

for word, tag in tagged_words:
    print(f"{word}\t\t{tag}")
