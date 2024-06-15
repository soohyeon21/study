# 17254

# a, b를 int() 안해주고 str() 상태로 풀면 틀린다.

import sys

n, m = map(int, sys.stdin.readline().split())

ipt = []
for _ in range(m):
    a, b, c = sys.stdin.readline().split()
    a, b = int(a), int(b)
    ipt.append((a, b, c))
ipt.sort(key=lambda x:(x[1], x[0]))

for i in range(m):
    print(ipt[i][2], end="")
