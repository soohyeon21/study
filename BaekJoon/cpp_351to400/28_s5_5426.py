# 5426

# 암호를 list에 안담고 곧바로 해독하는 방법도 있다.

# sqrt() 대신 **(1/2) 하는 방법도 있다.

import sys
import math

t = int(sys.stdin.readline())
for _ in range(t):
    enc = sys.stdin.readline().rstrip()
    n = int(math.sqrt(len(enc)))
    letter = [["" for x in range(n)] for xx in range(n)]
    for i in range(n):
        for j in range(n):
            letter[i][j] = enc[i*n+j]

    dec = ""
    for k in range(-1, -n-1, -1):
        for p in range(n):
            dec += letter[p][k]

    print(dec)
