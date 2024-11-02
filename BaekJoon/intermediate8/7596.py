# 7596

import sys

idx = 1
while (1):
    num = int(sys.stdin.readline())
    if (num == 0):
        break

    scenario = sorted([sys.stdin.readline().rstrip() for _ in range(num)])

    print(idx)
    print(*scenario, sep="\n")
    idx += 1
