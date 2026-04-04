# 31607

# or max()의 2배가 sum()과 같은지 판단.

import sys

num = sorted([int(sys.stdin.readline()) for _ in range(3)])

if (num[0]+num[1] == num[2]):
    print(1)
else:
    print(0)
