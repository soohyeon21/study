# 2693

# sort를 하고 -3번째 원소를 출력하는 방법도 있다.

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    case = list(map(int, sys.stdin.readline().split()))
    case1 = sorted(case, reverse=True)
    print(case1[2])
