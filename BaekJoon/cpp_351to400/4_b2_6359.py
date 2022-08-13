# 6359

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    jail = [0 for x in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n//i+1):
            if (jail[j*i] == 0):
                jail[j*i] = 1
            else:
                jail[j*i] = 0
    print(jail[1:].count(1))
