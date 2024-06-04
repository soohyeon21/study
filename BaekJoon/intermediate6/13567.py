# 13567

# directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
# 이렇게 해서 directions[idx], idx = (idx +- 1) % 4 하는 방법도 있다.

import sys

def go_toward(much, head, position):
    x, y = position[0], position[1]
    if (head == 0):
        x += much
    elif (head == 180):
        x -= much
    elif (head == 90):
        y += much
    elif (head == 270):
        y -= much

    return [x, y]

m, n = map(int, sys.stdin.readline().split())

head = 0
position = [0, 0]
state = True
for _ in range(n):
    cmd, num = sys.stdin.readline().split()
    if (cmd == "MOVE"):
        position = go_toward(int(num), head, position)
    elif (cmd == "TURN"):
        if (num == "0"):
            head += 90
        elif (num == "1"):
            head -= 90
        head %= 360

    if ((position[0] > m) or (position[0] < 0) or (position[1] > m) or (position[1] < 0)):
        state = False

if (state):
    print(*position)
else:
    print(-1)
