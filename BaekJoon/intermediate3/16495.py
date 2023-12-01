# 16495

import sys

word = sys.stdin.readline().rstrip()

n = len(word)
total = 0
for i in range(n):
    total += 26**(n-1-i)*(ord(word[i])-64)

print(total)
