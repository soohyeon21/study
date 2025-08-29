# 1010

# DP로도 풀 수 있다고 한다.

import sys

def nCk(n, k):
    rst = 1
    for nu in range(n, n-k, -1):
        rst *= nu
    for den in range(1, k+1):
        rst //= den
    return rst


t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    
    print(nCk(max(n, m), min(n, m)))
