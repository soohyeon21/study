# 30999

import sys

n, m = map(int, sys.stdin.readline().split())

cnt = 0
for _ in range(n):
    fp = sys.stdin.readline().rstrip()
    if (fp.count("O") > m//2):
        cnt += 1

print(cnt)
