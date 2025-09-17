# 13419

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    alp = sys.stdin.readline().rstrip()
    alp = alp*2 if (len(alp)%2 != 0) else alp
    
    h1 = alp[::2]
    h2 = alp[1::2]

    print(h1)
    print(h2)
