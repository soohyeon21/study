# 26849

import sys

n = int(sys.stdin.readline())

num = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    num.append(a/b)

print(min(num))
print(max(num))
print(sum(num))
