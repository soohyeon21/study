# 2566

import sys

table = []
for _ in range(9):
    table.append(list(map(int, sys.stdin.readline().split())))

row = 0
mmax = 0
for i in range(9):
    if (mmax < max(table[i])):
        row = i
        mmax = max(table[i])
column = table[row].index(mmax)

print(mmax)
print(row+1, column+1)
