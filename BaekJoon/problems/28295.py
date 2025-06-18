# 28295

import sys

head = 0
value = {1:90, 2:180, 3:-90}
for _ in range(10):
    order = int(sys.stdin.readline())
    head += value[order]

head += 360*3

print("NESW"[(head%360)//90])
