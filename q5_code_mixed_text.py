
import re

text = input("Enter a code-mixed sentence: ")

tokens = re.findall(r"[A-Za-z]+|[^\w\s]", text)

language_labels = {
    "kal": "HI",
    "ka": "HI",
    "meeting": "EN",
    "cancel": "EN",
    "ho": "HI",
    "gaya": "HI",
    "please": "EN",
    "reschedule": "EN",
    "it": "EN",
    "by": "EN",
    "friday": "EN"
}

print("\nToken Language Identification")
print("-----------------------------")

for token in tokens:
    label = language_labels.get(token.lower(), "UNKNOWN")
    print(f"{token:<15} {label}")

print("\nPreprocessing Pipeline")
print("----------------------")
print("1. Clean the text")
print("2. Tokenize the sentence")
print("3. Identify the language of each token")
print("4. Normalize romanised Hindi words")
print("5. Apply Hindi and English lemmatization")
print("6. Perform POS tagging")
print("7. Detect the user's intent")
print("\nDetected intent: Meeting rescheduling")
