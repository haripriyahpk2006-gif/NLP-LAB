
import nltk
from nltk.corpus import brown
from nltk import UnigramTagger, BigramTagger, word_tokenize

nltk.download('brown')
nltk.download('punkt')
nltk.download('punkt_tab')

# Load tagged sentences
tagged_sentences = brown.tagged_sents(categories='news')

# Split into training and testing data
size = int(len(tagged_sentences) * 0.9)
train_data = tagged_sentences[:size]
test_data = tagged_sentences[size:]

# Train Unigram and Bigram taggers
unigram_tagger = UnigramTagger(train_data)
bigram_tagger = BigramTagger(
    train_data,
    backoff=unigram_tagger
)

# Evaluate accuracy
accuracy = bigram_tagger.accuracy(test_data)
print(f"Tagger Accuracy: {accuracy * 100:.2f}%")

# Tag a new sentence
sentence = input("\nEnter a sentence: ")
tokens = word_tokenize(sentence)

result = bigram_tagger.tag(tokens)

print("\nWord\t\tPoS Tag (Stochastic)")
print("-" * 35)

for word, tag in result:
    print(f"{word}\t\t{tag}")

