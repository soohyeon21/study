# 9723

import sys

t = int(sys.stdin.readline())
for i in range(1, t+1):
    tri = sorted(list(map(int, sys.stdin.readline().split())))
    state = "YES" if (tri[0]**2 + tri[1]**2 == tri[2]**2) else "NO"
    print(f"Case #{i}: {state}")
