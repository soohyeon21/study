# 34666

import sys

q = int(sys.stdin.readline())

least = {1:100, 2:90, 3:95, 4:90, 5:80}
for _ in range(q):
    info = list(map(int, sys.stdin.readline().split()))

    state = True
    if (info[0] not in [1, 2]):
        state = False
    if (info[3] < 50):
        state = False

    cond1, cond2 = 0, 0
    for area in [1, 2]:
        if (info[area]*3 < least[info[0]]):
            cond1 += 1
        if (info[area] < 19+3):
            cond2 += 1
    if (not ((cond1 >= 2) or (cond2 >= 1))):
        state = False

    if (state):
        print('YES')
    else:
        print('NO')
