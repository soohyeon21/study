# 16676

import sys

n = int(sys.stdin.readline())
digit = "1"
stickers = 0

if (n < 10):
    stickers = 1
else:
    while (n >= int(digit)):
        digit = digit+"1"
    stickers = len(digit) -1

print(stickers)
