# 8674

# a x b 크기의 초콜릿을 1번만 쪼갰을 때의 두 조각의 크기의 차의 최소값은?

import sys

a, b = map(int, sys.stdin.readline().split())

if ((a%2 == 0) or (b%2 == 0)):
    print(0)
else:
    print(min(a, b))
