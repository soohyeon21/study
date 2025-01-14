# 14487

import sys

n = int(sys.stdin.readline())
edge = list(map(int, sys.stdin.readline().split()))

print(sum(edge)-max(edge))
