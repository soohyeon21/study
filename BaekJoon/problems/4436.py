# 4436

# set() 사용해도 됨.

import sys

while (1):
    n = sys.stdin.readline().rstrip()
    if (n == ''):
        break
    
    n = int(n)
    start = n
    cnt = 0
    num = {i:0 for i in range(10)}
    while (0 in num.values()):
        cnt += 1
        tmp = cnt*start
        for digit in str(tmp):
            num[int(digit)] += 1
        
    print(cnt)
