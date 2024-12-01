# 6718

import sys

MAX = 2**15
prime = [True for x in range(MAX+1)]
prime[0], prime[1] = False, False
for i in range(2, MAX):
    if (prime[i]):
        for j in range(i*i, MAX, i):
            prime[j] = False

while (1):
    n = int(sys.stdin.readline())
    if (n == 0):
        break

    cnt = 0
    for odd in range(3, n//2+1, 2):
        if (prime[odd] and prime[n-odd]):
            cnt += 1

    print(cnt)
