from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = ["playing", "running", "studies", "easily", "happiness"]

print("Stemming Results:")
for word in words:
    print(f"{word} -> {stemmer.stem(word)}")
