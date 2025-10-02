# 13901

# 이동 중 벽이나 방문한 지역, 장애물을 만나는 경우가 아니라면, 원래 가던 방향을 계속 유지한다.

import sys

r, c = map(int, sys.stdin.readline().split())
block = [tuple(map(int, sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline()))]
sr, sc = map(int, sys.stdin.readline().split())
d_order = list(map(int, sys.stdin.readline().split()))
heading = {1:(-1, 0), 2:(1, 0), 3:(0, -1), 4:(0, 1)}

room = {} # 1:방문함, -1:장애물, 0:방문안함
for row in range(r):
    for col in range(c):
        room[(row, col)] = room.setdefault((row, col), 0)
for b in block:
    room[b] = -1

now_coord = (sr, sc)
room[now_coord] = 1
now_dir = 0
blocked = 0
while (1):
    if (blocked == 4):
        break
    next_coord = (now_coord[0]+heading[d_order[now_dir]][0], now_coord[1]+heading[d_order[now_dir]][1])
    try:
        if (room[next_coord] == 0):
            now_coord = next_coord
            room[next_coord] = 1
            blocked = 0
        else:
            blocked += 1
            now_dir = (now_dir+1)%4
    except KeyError: # 방 밖의 좌표인 경우
        blocked += 1
        now_dir = (now_dir+1)%4

print(*now_coord)
