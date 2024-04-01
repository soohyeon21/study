# 26546

import sys

n = int(sys.stdin.readline())
for _ in range(n):
    string, i, j = sys.stdin.readline().split()
    i = int(i)
    j = int(j)
    print(string[:i]+string[j:])
