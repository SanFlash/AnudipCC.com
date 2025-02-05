sentence = "the quick brown fox jumps over the lazy dog"

word_counts = {}
for word in sentence.split():
    word_counts[word] = word_counts.get(word, 0) + 1

print("Word Frequencies:", word_counts)
