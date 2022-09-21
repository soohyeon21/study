# 14581

import sys

name = sys.stdin.readline().rstrip()
name = ":" + name + ":"
fan = ":fan:"
fname = fan + name + fan

print(fan*3)
print(fname)
print(fan*3)
