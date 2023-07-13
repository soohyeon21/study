# 6794

import sys

n = int(sys.stdin.readline())

cnt = 0
for i in range(n//2+1):
    a = i
    b = n-i
    if ((a <= 5) and (b <= 5)):
        cnt += 1
print(cnt)
