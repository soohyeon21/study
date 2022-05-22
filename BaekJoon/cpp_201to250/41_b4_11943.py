# 11943

# 아, 괜히 복잡하게 생각해버렸다.

import sys

apple = []
orange = []
for _ in range(2):
    a, b = map(int, sys.stdin.readline().split())
    apple.append(a)
    orange.append(b)

cnt = [apple[0] + orange[1], apple[1] + orange[0]]
print(min(cnt))
