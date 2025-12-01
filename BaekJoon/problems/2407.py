# 2407

# math.comb(a, b) # 동일 역할.

import sys

def nCk(n, k):
    k = min(n-k, k)
    num, deno = 1, 1
    for i in range(k):
        num *= (n-i)
    for j in range(k):
        deno *= (j+1)
    return num//deno


n, m = map(int, sys.stdin.readline().split())

print(nCk(n, m))
