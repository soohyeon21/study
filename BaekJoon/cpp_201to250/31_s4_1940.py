# 1940

import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
ns = list(map(int, sys.stdin.readline().split()))
cnt = 0

for i in range(n):
    if ((m - ns[i]) in ns):
        cnt += 1

print(cnt//2)
