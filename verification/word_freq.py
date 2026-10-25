from collections import Counter

sample_text = 'to be or not to be that is the question'
words = sample_text.split()
word_counts = Counter(words)
top_5 = word_counts.most_common(5)

for word, count in top_5:
    print(f'{word}: {count}')
