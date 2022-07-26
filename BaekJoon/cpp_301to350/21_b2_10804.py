# 10804

# reverse()를 쓰는 방법도 있다.

import sys

card = [x for x in range(1, 21)]
for _ in range(10):
    a, b = map(int, sys.stdin.readline().split())
    for i in range((b-a+1)//2):
        card[a-1+i], card[a+b-2 - (a-1+i)] = card[a+b-2 - (a-1+i)], card[a-1+i]
print(*card)
