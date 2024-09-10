# 5101

# An = a + (n-1)*d # (n-1)>=0 즉, (th-a)>=0이어야 한다.
# cf) 3 2 1

# 덧) 'the difference - this will be a non-zero integer' -> (d == 0)으로도 충분.

import sys

while (1):
    a, d, th = map(int, sys.stdin.readline().split())
    if ((a == 0) and (d == 0) and (th == 0)): # or (d == 0)
        break

    if (((th-a)%d == 0) and (th-a >= 0)):
        print(1+(th-a)//d)
    else:
        print("X")
