# 16770

import sys

n = int(sys.stdin.readline())

consume = [0 for i in range(1001)]
for _ in range(n):
    si, ti, bi = map(int, sys.stdin.readline().split())
    for occu in range(si, ti):
        consume[occu] += bi

print(max(consume))
