# 14652

# n은 필요 없었다고 한다.

import sys

n, m, k = map(int, sys.stdin.readline().split())

row = k//m
col = k%m
print(row, col)
