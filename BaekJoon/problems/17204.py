# 17204

import sys

n, k = map(int, sys.stdin.readline().split())
ai = {i:int(sys.stdin.readline()) for i in range(n)}

order = []
now = 0
for i in range(151):
    now = ai[now]
    order.append(now)
    if (now == k):
        break
    
if (k in order):
    print(order.index(k)+1)
else:
    print(-1)
