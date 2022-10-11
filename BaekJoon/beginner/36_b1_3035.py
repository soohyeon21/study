# 3035

# 겁 먹었던 것보다는 쉽게 풀렸다.

import sys

r, c, zr, zc = map(int, sys.stdin.readline().split())
scanner = []
new = []

for _ in range(r):
    scanner.append(sys.stdin.readline().rstrip())

for i in range(r):
    tmp = ""
    for j in range(c):
        tmp += scanner[i][j]*zc
    for k in range(zr):
        new.append(tmp)

for row in new:
    print(row)
