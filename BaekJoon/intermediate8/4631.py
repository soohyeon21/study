# 4631

import sys

idx = 1
while (1):
    n = int(sys.stdin.readline())
    if (n == 0):
        break

    names = [sys.stdin.readline().rstrip() for _ in range(n)]
    group = [[], []]

    for i in range(n):
        group[i%2].append(names[i])
    comb = group[0] + list(reversed(group[1]))

    print(f"SET {idx}")
    print(*comb, sep="\n")

    idx += 1
