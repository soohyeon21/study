# 20361

import sys

n, x, k = map(int, sys.stdin.readline().split())
game = [0 for i in range(n+1)]
game[x] = 1
for _ in range(k):
    a, b = map(int, sys.stdin.readline().split())
    game[a], game[b] = game[b], game[a]

print(game.index(1))
