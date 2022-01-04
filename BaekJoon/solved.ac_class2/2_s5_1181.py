# 1181

# key = lambda x: (len(x), x)

import sys

n = int(sys.stdin.readline())

words = []
for _ in range(n):
    words.append(sys.stdin.readline().rstrip())

words = list(set(words))

order = sorted(words, key = lambda x: (len(x), x))

for word in order:
    print(word)
