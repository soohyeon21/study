# 28431

import sys

socks = [int(sys.stdin.readline()) for _ in range(5)]

for one in list(set(socks)):
    if (socks.count(one)%2 == 1):
        print(one)
