# 17521

# 길게 볼 필요 없이, '오늘과 내일'의 가격만 보고 '오늘' 뭐할지 판단하면 된다.

import sys

n, w = map(int, sys.stdin.readline().split())
price = list(int(sys.stdin.readline()) for _ in range(n))

coin = 0
for i in range(n-1):
    if (price[i] < price[i+1]):
        coin += w//price[i]
        w %= price[i]
    elif (price[i] > price[i+1]):
        w += coin*price[i]
        coin = 0

w += price[-1]*coin

print(w)
