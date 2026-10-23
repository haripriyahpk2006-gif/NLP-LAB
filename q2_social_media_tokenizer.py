
import re

text = input("Enter a social-media post: ")

pattern = r"""
[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}       # Email
|[:;=8xX][-^']?[)(/DPp]               # Emoticons
|#[A-Za-z0-9_]+                       # Hashtags
|@[A-Za-z0-9_]+                        # Mentions
|\$[0-9]+(?:\.[0-9]+)?[kKmM]?         # Currency
|[A-Za-z]+(?=n't\b)                   # First part of can't
|n't\b                                # n't
|[A-Za-z]+(?:-[A-Za-z]+)*             # Words
|[0-9]+(?:\.[0-9]+)?                  # Numbers
|[^\w\s]                              # Punctuation
"""

tokens = re.findall(pattern, text, flags=re.IGNORECASE | re.VERBOSE)

print("\nTokens:")
for token in tokens:
    print(token)