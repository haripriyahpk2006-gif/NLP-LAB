from nltk.stem import PorterStemmer

# Create stemmer object
stemmer = PorterStemmer()

# List of words
words = ["playing", "running", "studies", "easily", "happiness"]

print("Stemming Results:")
for word in words:
    print(f"{word} -> {stemmer.stem(word)}")