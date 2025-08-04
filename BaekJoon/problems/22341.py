# 22341

# 원점에서 아래로 내려가는게 x, 오른쪽으로 가는게 y

# 문제를 잘 읽자.
# "만약 점이 종이의 경계나 밖에 있다면, 즉 X>=A이거나, Y>=B라면 이 점은 '무시'된다."
# "종이를 가로로 자를 때는 '위쪽을 남기고' 아래쪽을 버리고, 세로로 자를 때는 '왼쪽을 남기고' 오른쪽을 버린다."

import sys

n, c = map(int, sys.stdin.readline().split())

nx, ny = n, n
for _ in range(c):
    x, y = map(int, sys.stdin.readline().split())
    if ((x >= nx) or (y >= ny)):
        continue

    if (y*nx > ny*x):
        ny = y
    else:
        nx = x
            
print(nx*ny)
