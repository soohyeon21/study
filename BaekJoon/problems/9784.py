# 9784

import sys

t = int(sys.stdin.readline())
for idx in range(1, t+1):
    n, p, q = map(int, sys.stdin.readline().split())
    eggs = sorted(list(map(int, sys.stdin.readline().split())))

    ok = []
    for i in range(n):
        if (sum(ok, eggs[i]) <= q):
            ok.append(eggs[i])
        else:
            break

    boil = min(len(ok), p)

    print(f"Case {idx}: {boil}")
