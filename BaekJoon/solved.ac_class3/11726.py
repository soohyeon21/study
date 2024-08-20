# 11726

# DP

import sys

def nCk(n, k):
    tmp = 1
    for nt in range(n-k+1, n+1):
        tmp *= nt
    for kt in range(1, k+1):
        tmp //= kt
    return tmp


w = int(sys.stdin.readline())

cases = 0
for i in range(w//2+1):
    cases += nCk(w-i, i)

print(cases%10007)
