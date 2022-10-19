# 2605

import sys

n = int(sys.stdin.readline())
line = list(map(int, sys.stdin.readline().split()))
eat = []

for i in range(n):
    eat.insert(line[i], i+1)

eat = eat[::-1]
print(*eat)
