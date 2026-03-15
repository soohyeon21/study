# 28288

import sys

n = int(sys.stdin.readline())
sche = [sys.stdin.readline().rstrip() for _ in range(n)]

peop_day = {p:[] for p in range(n+1)}
for i in range(5):
    avail = 0
    for j in range(n):
        if (sche[j][i] == 'Y'):
            avail += 1
    peop_day[avail].append(i+1)

for p, d in reversed(peop_day.items()):
    if (len(d) != 0):
        print(*d, sep=',')
        break
