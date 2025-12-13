# 15115

# for문 말고, 수학적으로 최선의 m을 구할 수 있는 방법이 있는듯.

import sys

k, p, x = map(int, sys.stdin.readline().split())

least = x+k*p
for m in range(2, 10001):
    money = m*x + k/m*p
    least = min(least, money)
    if (least < money):
        break

print(f"{least:.3f}")
