# 4635

import sys

while (1):
    n = int(sys.stdin.readline())
    if (n == -1):
        break

    before = 0
    total = 0
    for _ in range(n):
        mp, elap = map(int, sys.stdin.readline().split())
        total += mp*(elap-before)
        before = elap
        
    print(f"{total} miles")
