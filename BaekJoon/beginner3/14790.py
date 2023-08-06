# 14790

import sys

t = int(sys.stdin.readline())
for cnt in range(1, t+1):
    n = int(sys.stdin.readline())
    for num in range(n, 0, -1):
        strnum = str(num)
        state = True
        for i in range(len(strnum)-1):
            if (int(strnum[i])>int(strnum[i+1])):
                state = False
                break
        if (state):
            print(f"Case #{cnt}: {strnum}")
            break
