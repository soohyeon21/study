# 31613

import sys

x = int(sys.stdin.readline())
n = int(sys.stdin.readline())

cnt = 0
while (1):
    r = x%3
    if (r == 0):
        x += 1
    elif (r == 1):
        x *= 2
    elif (r == 2):
        x *= 3
    cnt += 1
    
    if (x >= n):
        break

print(cnt)
