# 13236

import sys

n = int(sys.stdin.readline())

nlist = [n]
while (1):
    if (n == 1):
        break
    elif (n%2 == 0):
        n //= 2
    elif (n%2 != 0):
        n = n*3+1
    nlist.append(n)

print(*nlist)
