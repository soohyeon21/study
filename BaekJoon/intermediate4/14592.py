# 14592

import sys

n = int(sys.stdin.readline())
apc = []
for i in range(1, n+1):
    s, c, l = map(int, sys.stdin.readline().split())
    apc.append([s, c, l, i])
apc.sort(key=lambda x:(-x[0], x[1], x[2]))
print(apc[0][3])
