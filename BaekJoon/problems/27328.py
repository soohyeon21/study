# 27328

# A < B # -1
# A = B # 0
# A > B # 1

import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())

if (a < b):
    print(-1)
elif (a == b):
    print(0)
elif (a > b):
    print(1)
