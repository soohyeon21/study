# 9896

import sys

n = int(sys.stdin.readline())
binb = sys.stdin.readline().rstrip()

gray = binb[0]
for i in range(1, n):
    tmp = (int(binb[i-1])+int(binb[i]))%2
    gray += str(tmp)

print(gray)
