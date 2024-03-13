# 23375

# coords에 (1, 1), (1, -1)처럼 넣어놓고 나중에 r을 곱해서 더하는 방법도 있음.

import sys

x, y = map(int, sys.stdin.readline().split())
r = int(sys.stdin.readline())

coords = [(r, r), (r, -r), (-r, -r), (-r, r)]
for i in range(4):
    print(x+coords[i][0], y+coords[i][1])
