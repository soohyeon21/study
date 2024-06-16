# 1439

import sys

s = sys.stdin.readline().rstrip()

one = s.split("0")
zero = s.split("1")
cnt_one = 0
cnt_zero = 0
for o in one:
    if (o != ""):
        cnt_one += 1
for z in zero:
    if (z != ""):
        cnt_zero += 1

print(min(cnt_one, cnt_zero))
