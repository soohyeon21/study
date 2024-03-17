# 9613

# tcase = list()[1:] # 이렇게 하는 방법도 있다.

import sys

def gcf(a, b):
    while (b != 0):
        num = a % b
        a = b
        b = num
    return a

t = int(sys.stdin.readline())
for _ in range(t):
    tcase = list(map(int, sys.stdin.readline().split()))
    GCDs = []
    for i in range(1, len(tcase)):
        for j in range(i+1, len(tcase)):
            GCDs.append(gcf(tcase[i], tcase[j]))

    print(sum(GCDs))
