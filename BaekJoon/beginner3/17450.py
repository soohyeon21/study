# 17450

# 오... 문제를 잘못 읽었다.
# 5000원 이상일때 500원 할인해준다. 500원을 할인해줄때는 ZeroDivisionError를 고려하지 않아도 된다.

import sys

snu = "SNU"
snack = []
for i in range(3):
    p, w = map(int, sys.stdin.readline().split())
    pay = p*10-500 if p*10 >= 5000 else p*10
    ratio = w*10/pay #if pay != 0 else w*10
    snack.append((ratio, snu[i]))

snack.sort()
print(snack[-1][1])
