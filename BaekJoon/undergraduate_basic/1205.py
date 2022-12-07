# 1205

# 알쏭달쏭

import sys

n, score, p = map(int, sys.stdin.readline().split())

if (n == 0):
    print(1)
else:
    rank = list(map(int, sys.stdin.readline().split()))
    rank.append(score)
    rank.sort(reverse=True)
    tae = rank.index(score) + 1
    if (tae > p):
        print(-1)
    else:
        if ((n == p) and (score == rank[-1])):
            print(-1)
        else:
            print(tae)
