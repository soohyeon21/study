# 15905

import sys

n = int(sys.stdin.readline())
sol = sorted(list(tuple(map(int, sys.stdin.readline().split())) for _ in range(n)), key=lambda x:(-x[0], x[1]))

fifth = sol[4][0]
cnt = 0
for s in sol[5:]:
    if (s[0] == fifth):
        cnt += 1

print(cnt)
