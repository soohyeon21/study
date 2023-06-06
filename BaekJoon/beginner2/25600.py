# 25600

import sys

n = int(sys.stdin.readline())
score = [0 for x in range(n)]
for _ in range(n):
    a, d, g = map(int, sys.stdin.readline().split())
    if (a == d+g):
        score.append(2*a*(d+g))
    else:
        score.append(a*(d+g))

print(max(score))
