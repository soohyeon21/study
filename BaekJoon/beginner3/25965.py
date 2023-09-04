# 25965

# donate += max(0, price) 하는 방법도 있다.

import sys

n = int(sys.stdin.readline())
for _ in range(n):
    m = int(sys.stdin.readline())
    mission = [list(map(int, sys.stdin.readline().split())) for x in range(m)]
    k, d, a = map(int, sys.stdin.readline().split())
    
    donate = 0
    for case in mission:
        price = case[0]*k - case[1]*d + case[2]*a
        if (price > 0):
            donate += price

    print(donate)
