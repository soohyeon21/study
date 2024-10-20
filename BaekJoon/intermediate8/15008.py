# 15008

# sum(list[::2]), sum(list[1::2])

import sys

n = int(sys.stdin.readline())
nlist = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)

players = [0, 0]
for i in range(n):
    players[i%2] += nlist[i]

print(*players)
