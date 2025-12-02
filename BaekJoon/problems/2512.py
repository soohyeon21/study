# 2512

# 사실 이분 탐색 문제.

import sys

n = int(sys.stdin.readline())
budget = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

money = m//n
money += (m-money*n)//n

total = 0
while (1):
    total = sum(min(budget[i], money) for i in range(n))
    if (total == sum(min(budget[i], money+1) for i in range(n))):
        break
    if (sum(min(budget[i], money+1) for i in range(n)) > m):
        break
    money += 1

print(money)
