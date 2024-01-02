# 23246

import sys

n = int(sys.stdin.readline())
player = []
for _ in range(n):
    b, p, q, r = map(int, sys.stdin.readline().split())
    player.append((p*q*r, p+q+r, b))
player.sort(key=lambda x:(x[0], x[1], x[2]))
print(player[0][2], player[1][2], player[2][2])
