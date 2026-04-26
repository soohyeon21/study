# 31800

import sys

n = int(sys.stdin.readline())
profit = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    pure = profit[i] - (max(profit[:i]+profit[i+1:]) - price[i]) - price[i]
    print(pure, end=' ')
