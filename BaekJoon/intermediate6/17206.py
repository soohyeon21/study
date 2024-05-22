# 17206

import sys

t = int(sys.stdin.readline())
ns = list(map(int, sys.stdin.readline().split()))

for num in ns:
    total = 3*((num//3)*(num//3+1)//2) + 7*((num//7)*(num//7+1)//2) - 21*((num//21)*(num//21+1)//2)
    print(total)
