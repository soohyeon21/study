# 24079

# (X+Y)시간보다 (Z+0.5)시간이 크거나 같으면 1, 아니면 0.
# XYZ는 정수

import sys

xyz = list(int(sys.stdin.readline()) for _ in range(3))

total = sum(xyz[:2])*60
if (total <= xyz[2]*60+30):
    print(1)
else:
    print(0)
