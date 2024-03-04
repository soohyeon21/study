# 26068

import sys

n = int(sys.stdin.readline())

use = 0
for _ in range(n):
    left = sys.stdin.readline().rstrip()
    if (int(left[2:]) <= 90):
        use += 1

print(use)
