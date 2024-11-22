# 5046

import sys

n, b, h, w = map(int, sys.stdin.readline().split())

fee = []
for _ in range(h):
    p = int(sys.stdin.readline())
    stay = list(map(int, sys.stdin.readline().split()))

    for day in stay:
        if ((day >= n) and (p*n <= b)):
            fee.append(p*n)

if (len(fee) == 0):
    print("stay home")
else:
    print(min(fee))
