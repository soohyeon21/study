# 19602

import sys

tr = 0
for i in range(1, 4):
    n = int(sys.stdin.readline())
    tr += n * i

if (tr >= 10):
    print("happy")
else:
    print("sad")
