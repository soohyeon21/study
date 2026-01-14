# 34758

import sys

x, y = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())

for _ in range(n):
    xi, yi = map(int, sys.stdin.readline().split())
    if ((xi == x) or (yi == y)):
        print(0)
    else:
        print(1)
