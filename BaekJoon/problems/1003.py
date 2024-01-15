# 1003

import sys

def dp(n):
    f = [0, 1, 1] + [0 for _ in range(38)]
    if (n == 0):
        return 1, 0
    
    for i in range(3, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n-1], f[n]

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    cnt0, cnt1 = dp(n)
    print(cnt0, cnt1)
