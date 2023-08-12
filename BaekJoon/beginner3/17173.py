# 17173

import sys

n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
mul = []
for i in range(2, n+1):
    for exact in num:
        if ((i%exact == 0) and (i not in mul)):
            mul.append(i)
print(sum(mul))
