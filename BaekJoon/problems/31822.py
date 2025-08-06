# 31822

import sys

recode = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline())

cnt = 0
for _ in range(n):
    code = sys.stdin.readline().rstrip()
    if (recode[:5] == code[:5]):
        cnt += 1

print(cnt)
