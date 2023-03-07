# 27294

# 조건 하나로 if, 나머지는 else 처리해도 모든 경우가 포함된다.

import sys

t, s = map(int, sys.stdin.readline().split())
bob = 0

if (s or (t <= 11) or (t > 16)):
    bob = 280
elif ((not s) and (12 <= t <= 16)):
    bob = 320

print(bob)
