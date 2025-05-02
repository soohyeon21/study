# 22113

import sys

n, m = map(int, sys.stdin.readline().split())
bus = list(map(int, sys.stdin.readline().split()))
fee = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

total = 0
for i in range(1, m):
    total += fee[bus[i-1]-1][bus[i]-1]

print(total)
