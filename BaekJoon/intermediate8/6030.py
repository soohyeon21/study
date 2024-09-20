# 6030

# factor를 처음부터 아예 set으로 하는 것도 방법.

import sys

def findFactor(num):
    factors = []
    for i in range(1, int(num**0.5)+1):
        if ((num%i == 0) and (i not in factors)):
            factors.append(i)
            factors.append(num//i)
    return sorted(list(set(factors)))


p, q = map(int, sys.stdin.readline().split())
pcand, qcand = findFactor(p), findFactor(q)

for pone in pcand:
    for qone in qcand:
        print(pone, qone)
