# 1026

# ab = [[] for i in range(n)] # ab[[]*n] 은 안됨.

import sys

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
A.sort()
B.sort(reverse=True)

msum = 0
for i in range(n):
    msum += A[i]*B[i]

print(msum)
