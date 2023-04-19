# 15178

import sys

n = int(sys.stdin.readline())
for _ in range(n):
    num = list(map(int, sys.stdin.readline().split()))
    print(*num, end=" ")
    if (sum(num) == 180):
        print("Seems OK")
    else:
        print("Check")
