# 2720

import sys

t = int(sys.stdin.readline())
coins = [25, 10, 5, 1]

for _ in range(t):
    cent = []
    change = int(sys.stdin.readline())
    for coin in coins:
        cent.append(str(change // coin))
        change = change % coin
    print(' '.join(cent))
