# 9655

import sys

n = int(sys.stdin.readline())
win = ""

if (n % 2 != 0):
    win = "SK"
else:
    win = "CY"
print(win)
