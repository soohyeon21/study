# 1531

# 문제를 꼼꼼히 읽자.

# for문에 들어가야되는지 말아야되는지 잘 보기

import sys

n, m = map(int, sys.stdin.readline().split())

paint = [[0 for x in range(101)] for y in range(101)]
cnt = 0
for _ in range(n):
    lx, ly, rx, ry = map(int, sys.stdin.readline().split())
    for py in range(ly, ry+1):
        for px in range(lx, rx+1):
            paint[py][px] += 1

for numy in range(101):
    for numx in range(101):
        if (paint[numy][numx] > m):
            cnt += 1
print(cnt)
