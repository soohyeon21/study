# 3943

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    heil = [n]
    while (n != 1):
        if (n % 2 == 0):
            n = n//2
        else:
            n = n*3 + 1
        heil.append(n)
    print(max(heil))
