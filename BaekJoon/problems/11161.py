# 11161

# 중간에 in 한 사람이 더 많아서 건물 잔류 사람이 발생하는 경우도 있다.

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    m = int(sys.stdin.readline())
    
    already_in = 0
    current = 0
    for i in range(m):
        pin, pout = map(int, sys.stdin.readline().split())
        current += pin-pout
        if (current < 0):
            already_in += abs(current)
            current = 0
        
    print(already_in)
