# 17588

import sys

n = int(sys.stdin.readline())
nlist = [int(sys.stdin.readline()) for _ in range(n)]
ndict = {x:0 for x in range(1, nlist[-1]+1)}
for num in nlist:
    ndict[num] = 1

state = True
for key, value in ndict.items():
    if (value == 0):
        state = False
        print(key)

if (state):
    print("good job")
