# 34848

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())

    cnt = 0
    while (n > 1):
        if (n%2 == 1):
            cnt += 1
        n = n//2 + n%2
        
    print(cnt)
