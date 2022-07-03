# 11816

import sys

x = sys.stdin.readline().rstrip()
if (x[:2] == "0x"):
    x = int(x, 16)
elif (x[0] == "0"):
    x = int(x, 8)
x = int(x)
print(x)
