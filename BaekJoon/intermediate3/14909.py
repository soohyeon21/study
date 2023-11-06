# 14909

import sys

num = list(map(int, sys.stdin.readline().split()))

cnt = 0
for n in num:
    if (n > 0):
        cnt += 1

print(cnt)
