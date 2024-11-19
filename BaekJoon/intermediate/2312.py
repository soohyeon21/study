# 2312

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())

    prime = [True for x in range(n+1)]
    prime[0], prime[1] = False, False
    for i in range(2, int(n**0.5)+1):
        for j in range(2, n//i+1):
            prime[i*j] = False

    factor = []
    for num in range(2, n+1):
        if (prime[num] and (n%num == 0)):
            factor.append(num)

    fpair = []
    for f in factor:
        for e in range(1, 18):
            if ((n//f**e)%f != 0):
                fpair.append((f, e))
                break

    for pair in fpair:
        print(*pair)
