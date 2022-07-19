# 11109

# parallel = d + p여야 되는 거 아닐까. 병렬이라매!!!!

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    d, n, s, p = map(int, sys.stdin.readline().split())
    parallel = d + p*n
    series = n * s
    if (parallel < series):
        print("parallelize")
    elif (parallel > series):
        print("do not parallelize")
    else:
        print("does not matter")
