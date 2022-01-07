# 4562

# 앗 문제 잘못 읽었다;;

import sys

n = int(sys.stdin.readline())

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    if (x < y):
        print("NO BRAINS")
    else:
        print("MMM BRAINS")
