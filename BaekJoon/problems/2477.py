# 2477

# 신발끈 공식

# 참외밭에서 작은 사각형을 구하는 풀이도 있는 듯.

import sys

k = int(sys.stdin.readline())

coord = [(0, 0)]
x, y = 0, 0
for _ in range(6):
    dire, dist = map(int, sys.stdin.readline().split())
    if (dire == 1):
        x += dist
    elif (dire == 2):
        x -= dist
    elif (dire == 3):
        y -= dist
    elif (dire == 4):
        y += dist
    coord.append((x, y))
coord.append((0, 0))

sec1, sec2 = 0, 0
for i in range(6):
    sec1 += coord[i][0]*coord[i+1][1]
    sec2 += coord[i][1]*coord[i+1][0]

kmel = abs(sec1-sec2)//2 * k

print(kmel)
