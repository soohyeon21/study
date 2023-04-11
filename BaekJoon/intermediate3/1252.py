# 1252

import sys

b1, b2 = sys.stdin.readline().split()
bsum = int(b1, 2) + int(b2, 2)
print(bin(bsum)[2:])
