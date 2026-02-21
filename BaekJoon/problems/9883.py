# 9883

import sys

x, y = map(int, sys.stdin.readline().split())

bx = bin(x)[2:]
by = bin(y)[2:]
bx = bx.zfill(max(len(bx), len(by)))
by = by.zfill(max(len(bx), len(by)))

result = ''
for i in range(len(bx)):
    result += bx[i] + by[i]

print(int(result, 2))
