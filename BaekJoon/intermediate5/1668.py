# 1668

# def 만들고 trophy 내림차순/오름차순으로 각각 하는 방법도 있다.

import sys

n = int(sys.stdin.readline())

trophy = [int(sys.stdin.readline()) for _ in range(n)]

lcnt = 1
rcnt = 1
left1 = trophy[0]
right1 = trophy[-1]
for i in range(1, n):
    if (left1 < trophy[i]):
        lcnt += 1
        left1 = trophy[i]
    if (right1 < trophy[n-i-1]):
        rcnt += 1
        right1 = trophy[n-i-1]

print(lcnt)
print(rcnt)
