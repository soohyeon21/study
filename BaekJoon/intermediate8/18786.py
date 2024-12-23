# 18786

# 문제를 잘 읽자ㅎ
# "as long as one of the sides of the triangle is parallel to the x-axis and another side is parallel to the y-axis."

import sys

n = int(sys.stdin.readline())
coord = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

area = 0
for p1 in range(n):
    for p2 in range(p1+1, n):
        for p3 in range(p2+1, n):
            x1, y1 = coord[p1]
            x2, y2 = coord[p2]
            x3, y3 = coord[p3]
            if ((len(set([x1, x2, x3])) != 2) or (len(set([y1, y2, y3])) != 2)):
                continue
            
            area = max(area, abs((x1*y2 + x2*y3 + x3*y1) - (y1*x2 + y2*x3 + y3*x1)))

print(area)
