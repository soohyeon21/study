# 8891

# or 브루트포스 방법.

import sys

def S(n):
    return n*(n+1)//2

def findDotVal(p):
    k = p[0]+p[1]
    return S(k-2)+p[0]

def findCoord(dotval):
    before = 0
    for i in range(1, 450):
        if (S(i) >= dotval):
            before = i-1
            break
    k = before + 2
    a = dotval - S(before)
    b = k - a
    return (a, b)

def calDotVal(v1, v2):
    coord1 = findCoord(v1)
    coord2 = findCoord(v2)
    new_dotval = findDotVal((coord1[0]+coord2[0], coord1[1]+coord2[1]))
    return new_dotval


t = int(sys.stdin.readline())

for _ in range(t):
    v1, v2 = map(int, sys.stdin.readline().split())
    print(calDotVal(v1, v2))
