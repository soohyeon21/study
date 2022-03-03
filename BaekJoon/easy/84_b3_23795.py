# 23795

import sys

money = 0
while (True):
    n = int(sys.stdin.readline())
    if (n == -1):
        break

    money += n

print(money)
