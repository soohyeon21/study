# 17427

# f(n)과 g(n)은 완전히 다른 함수이다. 별개의 함수.

import sys

n = int(sys.stdin.readline())

gn = 0
for i in range(1, n+1):
    gn += i * (n//i)

print(gn)
