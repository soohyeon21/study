# 25991

# 세제곱근 구하기 1)**(1/3) 2)pow(, 1/3) 3)math.cbrt()

import sys
import math

n = int(sys.stdin.readline())
each = list(map(float, sys.stdin.readline().split()))
#one_side = sum(one**3 for one in each)**(1/3)
#one_side = pow(sum(one**3 for one in each), 1/3)
one_side = math.cbrt(sum(one**3 for one in each))
print(one_side)
