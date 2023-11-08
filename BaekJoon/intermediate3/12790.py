# 12790

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    nx = list(map(int, sys.stdin.readline().split()))
    hp = nx[0] + nx[4]
    mp = nx[1] + nx[5]
    of = nx[2] + nx[6]
    df = nx[3] + nx[7]
    fight = max(hp, 1) + 5*max(mp, 1) + 2*max(of, 0) + 2*df

    print(fight)
