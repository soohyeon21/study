# 9492

# math.ceil() 사용 대신, (t+1)//2를 하는 방법도 있다.

import sys
import math

while (1):
    t = int(sys.stdin.readline())
    if (t == 0):
        break

    tnum1 = math.ceil(t/2)
    t1 = [sys.stdin.readline().rstrip() for x in range(tnum1)]
    t2 = [sys.stdin.readline().rstrip() for y in range(t-tnum1)]

    for i in range(t-tnum1):
        print(t1[i])
        print(t2[i])
    if (tnum1 != t-tnum1):
        print(t1[tnum1-1])
