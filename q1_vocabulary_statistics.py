
import re

text = "The cat sat on the mat. The dog sat on the log."

# Extract words and ignore punctuation
tokens = re.findall(r"\b\w+\b", text)

# Count tokens
total_tokens = len(tokens)

# Count unique types
lowercase_types = set(word.lower() for word in tokens)
case_preserved_types = set(tokens)

# Calculate TTR
ttr = len(lowercase_types) / total_tokens

print("Original Text:", text)
print("Word Tokens:", tokens)
print("Total Tokens:", total_tokens)
print("Types (lowercase):", sorted(lowercase_types))
print("Number of lowercase types:", len(lowercase_types))
print("Types (case preserved):", sorted(case_preserved_types))
print("Number of case-preserved types:", len(case_preserved_types))
print("Type-Token Ratio:", round(ttr, 4))
print("TTR Percentage:", round(ttr * 100, 2), "%")