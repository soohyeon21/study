# 25966

import sys

n, m, q = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for x in range(n)]

for _ in range(q):
    query = list(map(int, sys.stdin.readline().split()))
    
    if (query[0] == 0):
        arr[query[1]][query[2]] = query[3]
    elif (query[1] == 1):
        arr[query[1]], arr[query[2]] = arr[query[2]], arr[query[1]]

for row in reversed(arr):
    print(*row)
