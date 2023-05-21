# 14219

# 3의 배수도 잘 캐치했고, n*m을 곱한 것도 굿!

import sys

n, m = map(int, sys.stdin.readline().split())

if (n*m % 3 == 0):
    print("YES")
else:
    print("NO")
