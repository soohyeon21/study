# 2605

import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
ans = []

for i in range(n):
    ans.insert(i-num[i], i+1)

for k in ans:
    print(k, end=' ')
