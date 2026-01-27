# 7947

import sys

z = int(sys.stdin.readline())

for _ in range(z):
    rgb = [0, 0, 0]
    
    for k in range(10):
        ipt = list(map(int, sys.stdin.readline().split()))
        for i in range(3):
            rgb[i] += ipt[i]

    print(int(rgb[0]/10+0.5), int(rgb[1]/10+0.5), int(rgb[2]/10+0.5))
