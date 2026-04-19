# 31776

import sys

n = int(sys.stdin.readline())

cnt = 0
for _ in range(n):
    ti = list(map(int, sys.stdin.readline().replace('-1', '121').split()))
    if ((sorted(ti) == ti) and (ti != [121]*3)):
        cnt += 1

print(cnt)
