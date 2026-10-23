import nltk
from nltk.corpus import brown
from nltk import UnigramTagger, word_tokenize
from nltk.tag import brill, brill_trainer

nltk.download('brown')
nltk.download('punkt')
nltk.download('punkt_tab')

tagged_sentences = brown.tagged_sents(categories='news')

size = int(len(tagged_sentences) * 0.9)
train_data = tagged_sentences[:size]
test_data = tagged_sentences[size:]

baseline_tagger = UnigramTagger(train_data)

baseline_accuracy = baseline_tagger.accuracy(test_data)
print(f"Baseline accuracy: {baseline_accuracy * 100:.2f}%")

templates = brill.brill24()


def train_brill(max_rules):
    trainer = brill_trainer.BrillTaggerTrainer(
        baseline_tagger,
        templates,
        trace=3
    )

    tagger = trainer.train(
        train_data,
        max_rules=max_rules
    )

    accuracy = tagger.accuracy(test_data)

    print(f"\nMaximum rules: {max_rules}")
    print(f"Brill accuracy: {accuracy * 100:.2f}%")
    print(f"Improvement: {(accuracy - baseline_accuracy) * 100:.2f} percentage points")

    print("\nLearned transformation rules:")
    rules = tagger.rules()

    for index, rule in enumerate(rules[:10], start=1):
        print(f"{index}. {rule}")

    return tagger


brill_tagger_10 = train_brill(10)

brill_tagger_30 = train_brill(30)

sentence = "They will fish for hours near the river bank"
tokens = word_tokenize(sentence)

print("\nTest sentence:", sentence)
print("Tagged output:")
print(brill_tagger_30.tag(tokens))
