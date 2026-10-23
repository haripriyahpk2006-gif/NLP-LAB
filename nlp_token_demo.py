text = "Natural Language Processing is fascinating. It helps computers understand human language. It is widely used in AI."
sentences = text.split('.')
sentences = [s.strip() for s in sentences if s.strip()]
print("Sentences:")
for i, sentence in enumerate(sentences, start=1):
    print(f"{i}.{sentence}")