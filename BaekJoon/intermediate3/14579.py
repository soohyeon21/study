# 14579

# 복잡하지 않은 풀이다.
# a=3, b=5인 경우로 직접 예제를 손으로 써보면 이해 갈 것.
# or just range(a, b+1)

import sys

a, b = map(int, sys.stdin.readline().split())

total = 1
for i in range(1,b+1):
    total *= i*(i+1)//2
for j in range(1, a):
    total //= j*(j+1)//2

print(total%14579)
