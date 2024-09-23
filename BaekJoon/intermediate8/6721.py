# 6721

import sys

n = int(sys.stdin.readline())
for _ in range(n):
    n1, n2 = sys.stdin.readline().split()
    print(int(str(int(n1[::-1])+int(n2[::-1]))[::-1]))
