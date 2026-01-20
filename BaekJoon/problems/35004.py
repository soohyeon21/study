# 35004

import sys

n = int(sys.stdin.readline())

cnt = 0
while (int(n) != 0):
    n = bin(n)[2:][::-1]
    n = int(n[:-1]+'0', 2)
    cnt += 1

print(cnt)
