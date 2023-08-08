# 14732

# 대여 장소가 직사각형의 형태라는 보장이 없다.

# rect list를 1로 채웠다면 .count(1)말고 sum()을 구하는 방법도 있다.
# 어차피 list는 0 or 1 이므로.

import sys

rectsize = 500
rect = [[0 for x in range(rectsize)] for y in range(rectsize)]
n = int(sys.stdin.readline())
for _ in range(n):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for xx in range(x1, x2):
        for yy in range(y1, y2):
            rect[yy][xx] = 1

cnt = 0
for i in range(rectsize):
    cnt += rect[i].count(1)

print(cnt)
