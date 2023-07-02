# 2875

# while or if

import sys
import math

n, m, k = map(int, sys.stdin.readline().split())
team = min(n//2, m)
rest = n-team*2 + m-team
if (rest < k):
    more = math.ceil((k-rest)/3)
    team -= more

print(team)
