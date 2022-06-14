# 4435

import sys

g = [1, 2, 3, 3, 4, 10]
s = [1, 2, 2, 2, 3, 5, 10]

t = int(sys.stdin.readline())
for k in range(1, t+1):
    gg = list(map(int, sys.stdin.readline().split()))
    ss = list(map(int, sys.stdin.readline().split()))
    gcnt = 0
    scnt = 0
    phrase = "No victor on this battle field"
    for i in range(6):
        gcnt += g[i] * gg[i]
    for j in range(7):
        scnt += s[j] * ss[j]

    if (gcnt > scnt):
        phrase = "Good triumphs over Evil"
    elif (gcnt < scnt):
        phrase = "Evil eradicates all trace of Good"

    print(f"Battle {k}: {phrase}")
