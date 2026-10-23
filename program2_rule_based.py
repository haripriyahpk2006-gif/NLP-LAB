

import nltk
from nltk import word_tokenize
from nltk.tag import RegexpTagger

nltk.download('punkt')
nltk.download('punkt_tab')

# Hand-written rules
patterns = [
    (r'.*ing$', 'VBG'),
    (r'.*ed$', 'VBD'),
    (r'.*es$', 'VBZ'),
    (r'.*ould$', 'MD'),
    (r".*'s$", 'NN$'),
    (r'.*s$', 'NNS'),
    (r'^-?[0-9]+(\.[0-9]+)?$', 'CD'),
    (r'^(The|the|A|a|An|an)$', 'DT'),
    (r'^(in|on|at|of|for|with)$', 'IN'),
    (r'.*ly$', 'RB'),
    (r'.*', 'NN')
]

rule_based_tagger = RegexpTagger(patterns)

sentence = input("Enter a sentence: ")
tokens = word_tokenize(sentence)

tagged_output = rule_based_tagger.tag(tokens)

print("\nWord\t\tPoS Tag (Rule-Based)")
print("-" * 35)

for word, tag in tagged_output:
    print(f"{word}\t\t{tag}")
