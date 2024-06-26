# 11317

import sys
import math

n = int(sys.stdin.readline())
for _ in range(n):
    a, b, c, s, t = map(int, sys.stdin.readline().split())
    
    xp = (-b+math.sqrt(b**2-4*a*c)) / (2*a)
    xm = (-b-math.sqrt(b**2-4*a*c)) / (2*a)
    
    if (((s <= xp <= t) or (s <= xm <= t)) and (math.sqrt(b**2-4*a*c) >= 0)):
        print("Yes")
    else:
        print("No")
