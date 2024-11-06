# 20124

import sys

n = int(sys.stdin.readline())

cand = []
for _ in range(n):
    name, score = sys.stdin.readline().split()
    cand.append((name, int(score)))

cand.sort(key=lambda x:(-x[1], x[0]))

print(cand[0][0])
