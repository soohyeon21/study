# 21191

import sys

n = int(sys.stdin.readline())
grid = [sys.stdin.readline().rstrip() for _ in range(n)]

state = True
## row check
for row in grid:
    if (row.count('W') != row.count('B')):
        state = False
    if (('WWW' in row) or ('BBB') in row): # less than 3
        state = False

## col check
for r in range(n):
    col = ''
    for c in range(n):
        col += grid[c][r]
    if (col.count('W') != col.count('B')):
        state = False
    if (('WWW' in col) or ('BBB' in col)): # less than 3
        state = False

if (state):
    print(1)
else:
    print(0)
