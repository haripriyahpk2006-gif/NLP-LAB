import nltk
from nltk import word_tokenize, pos_tag

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

sentence = (
    "The little girl quickly finished her homework "
    "before dinner."
)

tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

print("Sentence:", sentence)
print("\nWord\t\tPoS Tag")
print("-" * 35)

for word, tag in tagged:
    print(f"{word:<15}{tag}")

sentence2 = input("\nEnter another sentence: ")
print("\nTagged Output:")

for word, tag in pos_tag(word_tokenize(sentence2)):
    print(f"{word:<15}{tag}")

