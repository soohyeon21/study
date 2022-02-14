# 17869

import sys

def S(k):
    if (k % 2 ==0):
        return k//2
    else:
        return (k+1)

n = int(sys.stdin.readline())
cnt = 0

while (n != 1):
    n = S(n)
    cnt += 1

print(cnt)
