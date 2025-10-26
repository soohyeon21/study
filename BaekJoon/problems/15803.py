# 15803

import sys

coord = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]

d1 = (coord[1][1]-coord[0][1])/(coord[1][0]-coord[0][0]) if coord[1][0]!=coord[0][0] else 'zero'
d2 = (coord[2][1]-coord[1][1])/(coord[2][0]-coord[1][0]) if coord[2][0]!=coord[1][0] else 'zero'

if (d1 == d2):
    print("WHERE IS MY CHICKEN?")
else:
    print("WINNER WINNER CHICKEN DINNER!")
