# 13221

import sys

person = tuple(map(int, sys.stdin.readline().split()))

n = int(sys.stdin.readline())
cabs = {}
for _ in range(n):
    taxi = tuple(map(int, sys.stdin.readline().split()))
    dist = abs(person[0]-taxi[0]) + abs(person[1]-taxi[1])
    cabs[dist] = taxi

closest = min(cabs.keys())
print(cabs[closest][0], cabs[closest][1])
