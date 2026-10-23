
import nltk
from nltk.corpus import brown
from nltk.tag import hmm

nltk.download('brown')

# Load tagged sentences
tagged_sentences = brown.tagged_sents(categories='news')

# Split into training and testing data
size = int(len(tagged_sentences) * 0.9)
train_data = tagged_sentences[:size]
test_data = tagged_sentences[size:]

# Train the HMM tagger
trainer = hmm.HiddenMarkovModelTrainer()
hmm_tagger = trainer.train_supervised(train_data)

# Evaluate accuracy
accuracy = hmm_tagger.accuracy(test_data)
print(f"HMM Tagger Accuracy: {accuracy * 100:.2f}%")

# Tag a sample sentence
sentence = "They refuse to permit the strike".split()

print("\nTagged Output:", hmm_tagger.tag(sentence))

