
import nltk
from nltk import word_tokenize, pos_tag

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

sentence = input("Enter a sentence: ")

# Tokenization
tokens = word_tokenize(sentence)
print("\nTokens:", tokens)

# Part-of-Speech Tagging
tagged = pos_tag(tokens)

print("\nWord\t\tPoS Tag")
print("-" * 30)

for word, tag in tagged:
    print(f"{word}\t\t{tag}")

