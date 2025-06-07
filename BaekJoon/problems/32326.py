# 32326

import sys

color = [int(sys.stdin.readline()) for _ in range(3)]
cost = color[0]*3 + color[1]*4 + color[2]*5

print(cost)
