# 11134

# 중복되는 거는 더 뺄 수도 있겠다.

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n, c = map(int, sys.stdin.readline().split())
    days = 0
    if (n % c == 0):
        days = n//c
    else:
        days = n//c + 1
    print(days)
