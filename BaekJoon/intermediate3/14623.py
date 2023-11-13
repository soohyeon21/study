# 14623

import sys

b1 = int(sys.stdin.readline(), 2)
b2 = int(sys.stdin.readline(), 2)
#print(format(b1*b2, "b"))
b12 = bin(b1*b2)
print(b12[2:])
