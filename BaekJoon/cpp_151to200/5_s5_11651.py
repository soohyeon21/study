# 11651

# y를 먼저 넣고 sort만 하는 방법도 있다.(1순위: y, 2순위: x일 테니까.)

import sys

n = int(sys.stdin.readline())

dots = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    dots.append((x, y))

dots.sort(key=lambda x: (x[1], x[0]))

for xy in dots:
    print(xy[0], xy[1])
