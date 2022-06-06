# 10874

import sys

answer = [((i-1)%5) + 1 for i in range(1, 11)]
cnt = 0

n = int(sys.stdin.readline())
for j in range(n):
    write = list(map(int, sys.stdin.readline().split()))
    if (write == answer):
        print(j+1)
