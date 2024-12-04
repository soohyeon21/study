# 20833

# 공식을 이용하는 방법도 있다.

import sys

n = int(sys.stdin.readline())

total = 0
for i in range(1, n+1):
    total += i**3

print(total)
