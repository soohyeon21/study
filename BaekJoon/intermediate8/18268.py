# 18268

import sys

k, n = map(int, sys.stdin.readline().split())

pair = []
for _ in range(k):
    order = list(map(int, sys.stdin.readline().split()))
    for i in range(n-1):
        for j in range(i+1, n):
            if ((order[i], order[j]) not in pair):
                pair.append((order[i], order[j]))

cnt = 0
for p in pair:
    if ((p[1], p[0]) not in pair):
        cnt += 1

print(cnt)
