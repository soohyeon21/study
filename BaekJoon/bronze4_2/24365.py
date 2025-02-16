# 24365

import sys

bee = list(map(int, sys.stdin.readline().split()))
same = sum(bee)//3

cnt = 0
for i in range(2, 0, -1):
    tmp = bee[i]-same
    cnt += tmp
    bee[i-1] += tmp
    
print(cnt)
