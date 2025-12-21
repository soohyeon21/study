# 34543

import sys

n = int(sys.stdin.readline())
w = int(sys.stdin.readline())

score = n*10
if (n >= 3):
    score += 20
if (n == 5):
    score += 50
if (w > 1000):
    score = max(0, score-15)

print(score)
