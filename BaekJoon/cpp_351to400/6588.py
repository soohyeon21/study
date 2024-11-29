# 6588

# print("Goldbach's conjecture is wrong.") # 사실 없어도 됨.

import sys

MAX = 1000000
prime = [True for x in range(MAX+1)]
prime[0], prime[1] = False, False

for i in range(2, MAX):
    if (prime[i]):
        for i in range(i*i, MAX, i):
            prime[i] = False

while (1):
    n = int(sys.stdin.readline())
    if (n == 0):
        break
    
    for k in range(3, n, 2): # 여기가 핵심
        if (prime[k] and prime[n-k]):
            print(f"{n} = {k} + {n-k}")
            break
