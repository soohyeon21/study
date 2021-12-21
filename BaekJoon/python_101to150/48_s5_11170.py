# 11170

# or list에 str(num)을 다 넣어버리고 마지막에 한 번만 count + join

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    cnt = 0
    n, m = map(int, sys.stdin.readline().split())
    for num in range(n, m+1):
        snum = str(num)
        cnt += snum.count("0")
    print(cnt)
