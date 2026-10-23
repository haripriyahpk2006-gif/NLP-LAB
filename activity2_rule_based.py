
import nltk
from nltk import word_tokenize
from nltk.tag import RegexpTagger

nltk.download('punkt')
nltk.download('punkt_tab')

patterns = [
    (r'.*ing$', 'VBG'),                 # running
    (r'.*ed$', 'VBD'),                  # examined
    (r'.*ly$', 'RB'),                   # carefully
    (r'.*ous$', 'JJ'),                  # dangerous
    (r'.*able$', 'JJ'),                 # comfortable
    (r'.*ment$', 'NN'),                 # development
    (r'.*ness$', 'NN'),                 # happiness
    (r'^(The|the|A|a|An|an)$', 'DT'),
    (r'^(They|they|He|he|She|she|It|it)$', 'PRP'),
    (r'^(in|on|at|of|for|with|before|and)$', 'IN'),
    (r'.*', 'NN')                       # default
]

tagger = RegexpTagger(patterns)

paragraph = (
    "The scientists carefully examined the newly discovered "
    "species. They quickly noted its unusual behaviour "
    "and recorded their findings in a detailed report."
)

tokens = word_tokenize(paragraph)
tagged = tagger.tag(tokens)

print("Test Paragraph:\n", paragraph)
print("\nRule-Based Tagged Output:")

for word, tag in tagged:
    print(f"{word:<15}{tag}")

print("\nTotal tokens:", len(tagged))
print("Review the output and count the correct tags manually.")
print("Accuracy = (Correct tags / Total tokens) * 100")
