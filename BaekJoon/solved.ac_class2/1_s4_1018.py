# 1018

# for문이 어지럽드아아아아아

import sys

n, m = map(int, sys.stdin.readline().split())
square = []
color = 65

for _ in range(n):
    square.append(sys.stdin.readline().rstrip())

for i in range(m-7):
    for j in range(n-7):
        wcnt, bcnt = 0, 0
        for h in range(j, j+8):
            for w in range(i, i+8):
                if ((h+w)%2 == 0):
                    if (square[h][w] != "W"): # WBWB
                        wcnt += 1
                    if (square[h][w] != "B"): # BWBW
                        bcnt +=1
                if ((h+w)%2 == 1):
                    if (square[h][w] != "B"): # WBWB/BWBW
                        wcnt += 1
                    if (square[h][w] != "W"): # BWBW/WBWB
                        bcnt +=1
        color = min(wcnt, bcnt, color)

print(color)
