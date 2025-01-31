# 24087

# 처음 Acm에 250엔. Bcm 추가마다 100엔. Scm 이상이 되는 최소 금액은?

import sys

s = int(sys.stdin.readline())
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())

cash = 250
height = a
while (s > height):
    cash += 100
    height += b

print(cash)
