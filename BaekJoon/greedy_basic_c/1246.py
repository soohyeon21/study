# 1246

import sys

n, m = map(int, sys.stdin.readline().split())
pi = sorted([int(sys.stdin.readline()) for _ in range(m)], reverse=True)

egg = {}
for k in range(m):
    egg[pi[k]] = pi[k]*min(k+1, n)

best = sorted(egg.items(), key=lambda x:-x[1])[0]
print(*best)
