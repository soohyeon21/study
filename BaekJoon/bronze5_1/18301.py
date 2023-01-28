# 18301

# (operator '/'를 사용하고 math.floor() 사용하기) == (operator '//'를 사용하기)

import sys
from math import floor

n1, n2, n12 = map(int, sys.stdin.readline().split())
n = floor((n1+1)*(n2+1)/(n12+1) - 1)
print(n)
