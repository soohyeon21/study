# 10865

import sys

n, m = map(int, sys.stdin.readline().split())

pairs = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]
friends = {i:0 for i in range(1, n+1)}
for pair in pairs:
    friends[pair[0]] += 1
    friends[pair[1]] += 1

print(*friends.values(), sep="\n")
