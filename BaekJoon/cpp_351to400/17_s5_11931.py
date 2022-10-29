# 11931

import sys

n = int(sys.stdin.readline())

num = []
for _ in range(n):
    num.append(int(sys.stdin.readline()))
num.sort(reverse=True)
print(*num, sep="\n")
