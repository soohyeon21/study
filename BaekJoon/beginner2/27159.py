# 27159

import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

score = 0
small = num[0]
for i in range(1, n):
    if (num[i] != num[i-1]+1):
        score += small
        small = num[i]
score += small

print(score)
