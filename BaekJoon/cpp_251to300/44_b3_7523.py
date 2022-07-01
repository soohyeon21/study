# 7523

import sys

t = int(sys.stdin.readline())
for i in range(1, t+1):
    n, m = map(int, sys.stdin.readline().split())
    rst = (n+m)*(m-n+1)//2
    print(f"Scenario #{i}:\n{rst}\n")
