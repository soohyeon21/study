# 10953

# split(",") 말고 split(',')으로 하는 게 8ms 덜 소요된다.

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split(","))
    print(a + b)
