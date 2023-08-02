# 14545

# (l+1-i)를 하나 (i)를 하나 결국엔 같음.

import sys

p = int(sys.stdin.readline())
for _ in range(p):
    l = int(sys.stdin.readline())
    cnt = 0
    for i in range(1, l+1):
        cnt += (l+1-i) ** 2
    print(cnt)
