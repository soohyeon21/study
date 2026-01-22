# 35106

# or 그냥 .count() 사용.

import sys

n = int(sys.stdin.readline())
hand = list(map(int, sys.stdin.readline().split()))

cnt = {1:[], 2:[], 3:[]}
for i in range(3*n):
    cnt[hand[i]].append(i)

for h1 in range(1, 4):
    if (len(cnt[h1]) < n):
        print(h1)

for h2 in range(1, 4):
    if (len(cnt[h2]) > n):
        print(h2)
