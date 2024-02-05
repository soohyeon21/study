# 9417

import sys
from itertools import combinations

def gcf(a, b):
    while (b != 0):
        num = a%b
        a = b
        b = num
    return a

n = int(sys.stdin.readline())
for _ in range(n):
    test = list(map(int, sys.stdin.readline().split()))
    combs = combinations(test, 2)
    ans = 1
    for one in combs:
        ans = max(ans, gcf(one[0], one[1]))

    print(ans)
