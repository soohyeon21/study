# 34798

import sys

alarm = list(map(int, sys.stdin.readline().split(':')))
woke = list(map(int, sys.stdin.readline().split(':')))

if (alarm[0]*60+alarm[1] < woke[0]*60+woke[1]):
    print("YES")
else:
    print("NO")
