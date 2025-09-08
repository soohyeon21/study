# 25425

# worst = min(n, a-k+1)
# best = max(math.ceil((a-k)/m)+1)

import sys
import math

n, m, a, k = map(int, sys.stdin.readline().split())

best, worst = 0, 0

remain_teams = math.ceil((a-k)/m)
best = remain_teams + 1

if (a-k >= n-1):
    worst = n
else:
    worst = (a-k) + 1

print(worst, best)
