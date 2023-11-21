# 1929

import sys

m, n = map(int, sys.stdin.readline().split())

prime = [1 for _ in range(n+1)]
prime[0], prime[1] = 0, 0

for i in range(2, int(n**0.5)+2):
    for j in range(2, n//i+1):
        prime[i*j] = 0

for idx in range(m, n+1):
    if (prime[idx]):
        print(idx)
