# 13229

# nlist = [1, 5, 6, 3, 5, 9, 0, 3, 9, 1] 대신 [1, 6, 12, 15, 20, 29, 29, 32, 41, 42]로 만들면 더 빠르다.

import sys

n = int(sys.stdin.readline())
nlist = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    print(sum(nlist[start:end+1]))
