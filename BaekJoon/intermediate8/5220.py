# 5220

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n, valid = map(int, sys.stdin.readline().split())
    
    if ((bin(n)[2:].count("1")+valid)%2 == 0):
        print("Valid")
    else:
        print("Corrupt")
