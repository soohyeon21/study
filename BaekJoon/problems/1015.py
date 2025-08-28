# 1015

import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

work = [[a[i], i] for i in range(n)]
work.sort(key=lambda x:(x[0], x[1]))

for k in range(n):
    work[k].append(k)
work.sort(key=lambda x:x[1])

for p in range(n):
    print(work[p][2], end=' ')
