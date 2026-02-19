# 9849

#
# sol1) python3 시간초과, pypy3 정답(892480KB, 2480ms)
# 전체 평면에서 하나씩 확인
#
##import sys
##
##n = int(sys.stdin.readline())
##
##plane = [[0 for i1 in range(10001)] for i2 in range(10001)]
##
##for _ in range(n):
##    x1, x2, y1, y2 = map(int, sys.stdin.readline().split())
##    for ty in range(y1, y2):
##        for tx in range(x1, x2):
##            plane[ty][tx] += 1
##
##area = 0
##for i in range(10001):
##    area += plane[i].count(n)
##
##print(area)



#
# sol2) python3 정답(32412KB, 36ms)
# 시작&끝의 min・max
#
import sys

n = int(sys.stdin.readline())

lx, rx, uy, dy = 0, 10000, 10000, 0
for _ in range(n):
    x1, x2, y1, y2 = map(int, sys.stdin.readline().split())
    lx = max(lx, x1)
    rx = min(rx, x2)
    uy = min(uy, y2)
    dy = max(dy, y1)

if ((lx < rx) and (dy < uy)):
    print((rx-lx)*(uy-dy))
else:
    print(0)
