# 2979

import sys

a, b, c = map(int, sys.stdin.readline().split())
chk = [0 for x in range(101)]

for _ in range(3):
    x, y = map(int, sys.stdin.readline().split())
    for i in range(x, y):
        chk[i] += 1
coin = chk.count(1)*a + chk.count(2)*2*b + chk.count(3)*3*c
print(coin)
