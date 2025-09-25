# 8911

import sys

def whereIsTurtle(order, head, coord):
    poss_head = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    if (order == "F"):
        coord = (coord[0]+head[0], coord[1]+head[1])
    elif (order == 'B'):
        coord = (coord[0]-head[0], coord[1]-head[1])
    elif (order == 'L'):
        idx = poss_head.index(head)
        head = poss_head[(idx-1+4)%4]
    elif (order == 'R'):
        idx = poss_head.index(head)
        head = poss_head[(idx+1+4)%4]
    return head, coord


t = int(sys.stdin.readline())

for _ in range(t):
    move = sys.stdin.readline().rstrip()
    head = (0, 1)
    coord = (0, 0)

    visited = [(0, 0)]
    for order in move:
        head, coord = whereIsTurtle(order, head, coord)
        visited.append(coord)

    minx, miny, maxx, maxy = 0, 0, 0, 0
    for c in visited:
        minx = min(c[0], minx)
        miny = min(c[1], miny)
        maxx = max(c[0], maxx)
        maxy = max(c[1], maxy)

    print(abs(minx-maxx)*abs(miny-maxy))
