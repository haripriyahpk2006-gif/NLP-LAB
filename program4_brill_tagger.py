
import nltk
from nltk.corpus import brown
from nltk import UnigramTagger, word_tokenize
from nltk.tag import brill, brill_trainer

nltk.download('brown')
nltk.download('punkt')
nltk.download('punkt_tab')

# Load tagged sentences
tagged_sentences = brown.tagged_sents(categories='news')

# Split into training and testing data
size = int(len(tagged_sentences) * 0.9)
train_data = tagged_sentences[:size]
test_data = tagged_sentences[size:]

# Initial baseline tagger
baseline_tagger = UnigramTagger(train_data)

print(
    f"Baseline Accuracy: "
    f"{baseline_tagger.accuracy(test_data) * 100:.2f}%"
)

# Define transformation rule templates
templates = brill.brill24()

# Train Brill tagger
trainer = brill_trainer.BrillTaggerTrainer(
    baseline_tagger,
    templates,
    trace=0
)

brill_tagger = trainer.train(
    train_data,
    max_rules=20
)

# Evaluate accuracy
print(
    f"Brill Tagger Accuracy: "
    f"{brill_tagger.accuracy(test_data) * 100:.2f}%"
)

# Tag a new sentence
sentence = input("\nEnter a sentence: ")
tokens = word_tokenize(sentence)

print("\nTagged Output:", brill_tagger.tag(tokens))

