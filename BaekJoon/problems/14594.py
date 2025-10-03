# 14594

# 벽을 부숴도 방번호는 1~N까지 유지된다.

import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
xy = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]

wall = {i:1 for i in range(1, n)}
for x, y in xy:
    for crash in range(x, y):
        wall[crash] = 0

room = sum(wall.values())+1

print(room)
