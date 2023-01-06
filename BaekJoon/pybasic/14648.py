# 14648

import sys

n, q = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
for _ in range(q):
    que = list(map(int, sys.stdin.readline().split()))
    if (que[0] == 1):
        print(sum(arr[que[1]-1:que[2]]))
        arr[que[1]-1], arr[que[2]-1] = arr[que[2]-1], arr[que[1]-1]
    elif (que[0] == 2):
        print(sum(arr[que[1]-1:que[2]]) - sum(arr[que[3]-1:que[4]]))
