# 33753

import sys
import math

a, b, c = map(int, sys.stdin.readline().split())
t = int(sys.stdin.readline())

fee = 0
if (t <= 30):
    fee = a
elif (t > 30):
    fee = a + math.ceil((t-30)/b)*c

print(fee)
