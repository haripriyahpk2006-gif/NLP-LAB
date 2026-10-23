import nltk
from nltk.corpus import brown
from nltk import UnigramTagger, BigramTagger

nltk.download('brown')


def evaluate_taggers(category, train_ratio):
    tagged_sentences = brown.tagged_sents(categories=category)

    size = int(len(tagged_sentences) * train_ratio)
    train_data = tagged_sentences[:size]
    test_data = tagged_sentences[size:]

    if not train_data or not test_data:
        print("Not enough data for this split.")
        return

    unigram_tagger = UnigramTagger(train_data)

    bigram_tagger = BigramTagger(
        train_data,
        backoff=unigram_tagger
    )

    unigram_accuracy = unigram_tagger.accuracy(test_data)
    bigram_accuracy = bigram_tagger.accuracy(test_data)

    print(f"\nCategory: {category}")
    print(f"Training percentage: {train_ratio * 100:.0f}%")
    print(f"Unigram accuracy: {unigram_accuracy * 100:.2f}%")
    print(f"Bigram accuracy:  {bigram_accuracy * 100:.2f}%")

    return bigram_tagger


evaluate_taggers('news', 0.9)
evaluate_taggers('news', 0.5)

evaluate_taggers('romance', 0.9)

tagged_sentences = brown.tagged_sents(categories='news')
size = int(len(tagged_sentences) * 0.9)
train_data = tagged_sentences[:size]

unigram_tagger = UnigramTagger(train_data)
bigram_tagger = BigramTagger(
    train_data,
    backoff=unigram_tagger
)

sentence = input("\nEnter a sentence to tag: ")
tokens = nltk.word_tokenize(sentence)

print("\nTagged sentence:")
print(bigram_tagger.tag(tokens))

