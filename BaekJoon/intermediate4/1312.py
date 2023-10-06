# 1312

# a/b를 한 후 소수점 아래 자리를 찾는 방법은 OverflowError 발생.
# python은 일정 자리까지만 나눗셈 계산을 하기 때문에 해당 문제는 나눗셈을 직접 구현해야 한다.

import sys

a, b, n = map(int, sys.stdin.readline().split())

ans = 0
for i in range(n):
    a = (a%b)*10
    ans = a//b

print(ans)
