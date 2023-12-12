# 18883

# 경우를 나누어 print(number) 하거나 print(number, end="") 하는 방법도 있다.

import sys

n, m = map(int, sys.stdin.readline().split())
num = [[x for x in range(a*m+1, a*m+m+1)] for a in range(n)]

for one in num:
    print(*one)
