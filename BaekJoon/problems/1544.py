# 1544

import sys

n = int(sys.stdin.readline())

cycle = []
for _ in range(n):
    check = sys.stdin.readline().rstrip()

    if (len(cycle) == 0):
        cycle.append(check*2)

    state = False
    for cword in cycle:
        if (check in cword):
            state = True

    if (not state):
        cycle.append(check*2)

print(len(cycle))
