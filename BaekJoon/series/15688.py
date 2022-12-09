# 15688

import sys

n = int(sys.stdin.readline())
num = []
for _ in range(n):
    num.append(int(sys.stdin.readline()))
num.sort()

print(*num, sep="\n")
