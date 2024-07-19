# 1436

# num=665에서 시작하면 n=1,2 고려하지 않아도 된다.

import sys

n = int(sys.stdin.readline())
idx = 2
num = 1666

while (1):
    if (n == 1):
        print(666)
        break
    elif (n == 2):
        print(1666)
        break
    
    num += 1
    if ("666" in str(num)):
        idx += 1

    if (idx == n):
        print(num)
        break
