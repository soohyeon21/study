# 2847

import sys

n = int(sys.stdin.readline())
num = [int(sys.stdin.readline()) for x in range(n)]
cnt = 0

for i in range(-1, -n, -1):
    if (num[i-1] >= num[i]):
        cnt += num[i-1] - num[i] + 1
        num[i-1] = num[i] - 1

print(cnt)
