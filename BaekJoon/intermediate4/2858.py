# 2858

# random하게 모든 수를 살펴볼 필요가 없다. 범위를 줄여보도록 하자.

import sys

def findLW(red, brown):
    inner_r = red//2-2
    for i in range(1, inner_r//2+1):
        if (i*(inner_r-i) == brown):
            print(max(i, inner_r-i)+2, min(i, inner_r-i)+2)
            return

r, b = map(int, sys.stdin.readline().split())

findLW(r, b)
