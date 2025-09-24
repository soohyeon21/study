# 2980

import sys

n, l = map(int, sys.stdin.readline().split())
signal = {}
for _ in range(n):
    t, r, g = map(int, sys.stdin.readline().split())
    signal[t] = (r, g)

spent = 0
pos = 0
while (1):
    if (pos == l):
        break
    
    if (pos not in signal.keys()):
        pos += 1
        spent += 1
    else: # 신호등 신호 확인 필요
        if (spent%(signal[pos][0]+signal[pos][1]) >= signal[pos][0]):
            pos += 1
        spent += 1

print(spent)
