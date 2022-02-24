# 21300

import sys

bottles = list(map(int, sys.stdin.readline().split()))
bsum = sum(bottles)

print(bsum * 5)
