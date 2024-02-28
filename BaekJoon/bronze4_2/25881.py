# 25881

import sys

first, addit = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())
for _ in range(n):
    energy = int(sys.stdin.readline())
    charge = min(energy, 1000)*first + (max(energy, 1000)-1000)*addit
    print(energy, charge)
