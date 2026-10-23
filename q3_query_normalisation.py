
import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download("wordnet", quiet=True)
nltk.download("omw-1.4", quiet=True)

words = ["running", "ran", "runs", "runner", "runners"]

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

print(f"{'Word':<12}{'Porter Stem':<15}{'Lemma'}")
print("-" * 40)

for word in words:
    stem = stemmer.stem(word)
    if word in ["running", "ran", "runs"]:
        lemma = lemmatizer.lemmatize(word, pos="v")
    else:
        lemma = lemmatizer.lemmatize(word, pos="n")

    print(f"{word:<12}{stem:<15}{lemma}")

print("\nQuery: run")
print("Words with lemma 'run': running, ran, runs")
