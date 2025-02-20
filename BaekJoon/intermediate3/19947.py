# 19947

# 투자 A,B,C가 섞여서 진행될 수 있다.

import sys

h, y = map(int, sys.stdin.readline().split())

money = [h for _ in range(y+1)]
rate = {1:0.05, 3:0.2, 5:0.35}

for year in range(1, y+1):
    for term in [1, 3, 5]:
        if (0 <= year-term):
            money[year] = max(money[year], int(money[year-term]*(1+rate[term])))

print(money[-1])
