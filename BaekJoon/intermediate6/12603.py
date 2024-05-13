# 12603

# y가 range(x+1, i)라서 사실 min, max 안써도 되긴 했다.

import sys

n = int(sys.stdin.readline())
for idx in range(1, n+1):
    c = int(sys.stdin.readline())
    i = int(sys.stdin.readline())
    p = list(map(int, sys.stdin.readline().split()))

    state = False
    for x in range(i):
        for y in range(x+1, i):
            if (p[x]+p[y] == c):
                print(f"Case #{idx}: {min(x, y)+1} {max(x, y)+1}")
                state = True
                break
        if (state):
            break
