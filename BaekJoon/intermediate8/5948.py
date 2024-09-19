# 5948

import sys

n = int(sys.stdin.readline())

repeat = []
cnt = 0
while (1):
    middle = int(str(n).zfill(4)[1:3])
    square = middle**2
    cnt += 1
    if (square in repeat):
        print(cnt)
        break
    repeat.append(square)
    n = square
