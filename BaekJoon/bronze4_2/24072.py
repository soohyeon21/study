# 24072

# 사람1: A일 후 오전에 도착 ~ B일 후 오전에 출발
# 사람2: C일 후 오후에 도착
# 서로 만나려면 조건은?

import sys

a, b, c = map(int, sys.stdin.readline().split())

if ((a <= c) and (c < b)):
    print(1)
else:
    print(0)
