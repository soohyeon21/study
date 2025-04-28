# 30017

import sys

patty, cheese = map(int, sys.stdin.readline().split())

height = min(patty-1, cheese)*2+1
print(height)
