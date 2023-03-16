# 2991

import sys

a, b, c, d = map(int, sys.stdin.readline().split())
man = list(map(int, sys.stdin.readline().split()))

for i in range(3):
    cnt = 0
    
    tmp1 = man[i] % (a+b)
    if (1 <= tmp1 <= a):
        cnt += 1

    tmp2 = man[i] % (c+d)
    if (1 <= tmp2 <= c):
        cnt += 1

    print(cnt)
