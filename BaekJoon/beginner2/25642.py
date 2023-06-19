# 25642

# 다섯 손가락 이상을 펴야 하는 사람이 패배한다.

import sys

a, b = map(int, sys.stdin.readline().split())

while (1):
    b += a
    if (b > 4):
        print("yt")
        break
    a += b
    if (a > 4):
        print("yj")
        break
