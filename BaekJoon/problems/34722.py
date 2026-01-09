# 34722

# 조건 범위 주의!

import sys

n = int(sys.stdin.readline())

go = 0
for _ in range(n):
    s, c, a, r = map(int, sys.stdin.readline().split())
    if ((s >= 1000) or (c >= 1600) or (a >= 1500) or (0 < r <= 30)):
        go += 1

print(go)
