# 14039

import sys

square = [list(map(int, sys.stdin.readline().split())) for x in range(4)]

row1 = sum(square[0])
rstate = True
for i in range(1, 4):
    if (sum(square[i]) != row1):
        rstate = False
        break
        
col1 = sum(square[y][0] for y in range(4))
cstate = True
for j in range(1, 4):
    col = 0
    for k in range(4):
        col += square[k][j]
    if (col != col1):
        ctate = False
        break

if (rstate and cstate):
    print("magic")
else:
    print("not magic")
