# 2910

import sys

n, c = map(int, sys.stdin.readline().split())
msg = list(map(int, sys.stdin.readline().split()))

mdict = {}
for i in range(n):
    mdict[msg[i]] = mdict.setdefault(msg[i], [0, i])
    mdict[msg[i]][0] += 1

bsort = sorted(list(mdict.items()), key=lambda x:(-x[1][0], x[1][1]))
for one in bsort:
    for many in range(one[1][0]):
        print(one[0], end=" ")
