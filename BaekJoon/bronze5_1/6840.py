# 6840

import sys

bowl = []
for _ in range(3):
    w = int(sys.stdin.readline())
    bowl.append(w)

bowl.sort()
print(bowl[1])
