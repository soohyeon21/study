# 14729

import sys

n = int(sys.stdin.readline())

score = sorted([float(sys.stdin.readline()) for _ in range(n)])
for i in range(7):
    print(f"{score[i]:.3f}")
