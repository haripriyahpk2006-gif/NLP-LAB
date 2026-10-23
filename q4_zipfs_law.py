
total_tokens = 2_000_000
vocabulary_types = 50_000
most_frequent_word = "the"
frequency_rank_1 = 120_000

k = frequency_rank_1

ranks = [1, 2, 10, 100, 50_000]

print("Zipf's Law Frequency Estimation")
print("--------------------------------")
print("Total tokens:", total_tokens)
print("Vocabulary types:", vocabulary_types)
print("Most frequent word:", most_frequent_word)
print("Rank 1 frequency:", frequency_rank_1)
print("\nEstimated frequencies:")

for rank in ranks:
    frequency = k / rank
    print(f"Rank {rank}: {frequency:.2f}")

print("\nMeaning:")
print("Many words occur rarely, creating a long tail.")
print("Models may struggle with rare or unseen words.")
