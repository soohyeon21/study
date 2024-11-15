# 20256

import sys

n = int(sys.stdin.readline())

for _ in range(n):
    x = int(sys.stdin.readline())

    state = False
    for i in range(1, int(x**0.5)+1):
        if ((x%i == 0) and (x%(x//i) == 0)):
            if (2*i >= x//i):
                state = True
                break
            
    if (state):
        print(1)
    else:
        print(0)
