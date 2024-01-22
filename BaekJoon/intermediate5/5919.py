# 5919

import sys

n = int(sys.stdin.readline())
piles = [int(sys.stdin.readline()) for _ in range(n)]

equal = sum(piles)//n
move = sum(abs(equal-pile) for pile in piles)//2

print(move)
