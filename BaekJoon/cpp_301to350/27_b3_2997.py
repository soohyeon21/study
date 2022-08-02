# 2997

import sys

order = list(map(int, sys.stdin.readline().split()))
order.sort()

ans = 0
d1 = order[1] - order[0]
d2 = order[2] - order[1]
if (d1 == d2):
    ans = order[2] + d1
elif (d1*2 == d2):
    ans = order[1] + d1
elif (d1 == d2*2):
    ans = order[0] + d2

print(ans)
