# 11179

import sys

n = int(sys.stdin.readline())

base2 = bin(n)[2:]
print(int(base2[::-1], 2))
