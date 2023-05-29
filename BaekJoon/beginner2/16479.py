# 16479

# d1-d2가 맞지만, 제곱이 되면서 상관없어지나보다.

import sys

k = int(sys.stdin.readline())
d1, d2 = map(int, sys.stdin.readline().split())
h2 = k**2 - ((d2-d1)/2)**2
print(h2)
