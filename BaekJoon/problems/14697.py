# 14697

import sys

a, b, c, n = map(int, sys.stdin.readline().split())

state = False
for ai in range(int(n//a)+1):
    for bi in range(int(n//b)+1):
        for ci in range(int(n//c)+1):
            if (ai*a + bi*b + ci*c == n):
                state = True

print(int(state))
