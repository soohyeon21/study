# 14471

import sys

n, m = map(int, sys.stdin.readline().split())
card = sorted([tuple(map(int, sys.stdin.readline().split())) for _ in range(m)], key=lambda x:-x[0])

cnt = 0
yen = 0
for i in range(m):
    if (cnt >= m-1):
        break
    
    if (card[i][0] < n):
        yen += n - card[i][0]
    cnt += 1

print(yen)
