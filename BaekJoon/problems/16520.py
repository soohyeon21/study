# 16520

import sys

a, b, k = map(int, sys.stdin.readline().split())

cnt = 0
for num in range(a, b+1):
    allBase = True
    for base in range(2, k+1):
        if ((num%base == 0) and (num != 0)): # 중요 조건
            allBase = False
            break
        altered = []
        cook = num
        while (cook != 0):
            altered.append(cook%base)
            cook //= base
        if (altered != altered[::-1]):
            allBase = False
            break

    if (allBase):
        cnt += 1

print(cnt)
