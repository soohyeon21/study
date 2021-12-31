# 11050

# 드디어 factorial을 써봤다!!

import sys
from math import factorial

n, k = map(int, sys.stdin.readline().split())

com = factorial(n) // (factorial(k) * factorial(n-k))
print(com)
