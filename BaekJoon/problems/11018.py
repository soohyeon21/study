# 11018

# "Each data sets should be followed by a blank line."

import sys

k = int(sys.stdin.readline())
for idx in range(1, k+1):
    print(f"Data Set {idx}:")

    n, m = sys.stdin.readline().split()
    stages = [tuple(map(float, sys.stdin.readline().split())) for i in range(int(n))] # (mi, ti, fi)
    
    weight = float(m) + sum(val1 for val1, val2, val3 in stages)
    g = 9.81
    height = 0
    vi = 0
    
    for i in range(int(n)): # for mi, ti, fi in stages:
        mi, ti, fi = stages[i][0], stages[i][1], stages[i][2]
        ai = fi/weight - 9.81
        height += vi*ti + 0.5*ai*ti**2
        vi += ai*ti
        weight -= mi
        
    print(f"{height:.2f}\n")
