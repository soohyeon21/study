# 14011

import sys

n, m = map(int, sys.stdin.readline().split())
cost = list(map(int, sys.stdin.readline().split()))
payoff = list(map(int, sys.stdin.readline().split()))

possible = []
for i in range(n):
    if (cost[i] < payoff[i]):
        possible.append((cost[i], payoff[i]))
possible.sort(key=lambda x:x[0])

for j in range(len(possible)):
    if (possible[j][0] <= m):
        m += possible[j][1]-possible[j][0]
    else:
        break

print(m)
