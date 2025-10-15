# 30889

import sys

n = int(sys.stdin.readline())

seat = [['.' for x in range(20)] for y in range(10)]

for i in range(n):
    pos = sys.stdin.readline().rstrip()
    row = ord(pos[0])-65
    col = int(pos[1:])-1
    seat[row][col] = 'o'

for j in range(10):
    print(*seat[j], sep='')
