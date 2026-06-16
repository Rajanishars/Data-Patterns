from collections import Counter
n = int(input())
lines = [input() for _ in range(n)]
for line in lines:
    letters = [c for c in line if c.isalpha()]
    if not letters:
        continue
    counts = Counter(letters)
    max_freq = max(counts.values())
    best_letters = [char for char, freq in counts.items() if freq == max_freq]
    best_letters.sort(key=lambda x: (x.islower(), x))
    print("".join(best_letters))
