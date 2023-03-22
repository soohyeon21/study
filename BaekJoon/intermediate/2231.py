# 2231

# for문 반복 횟수에 겁먹지 말자.

# sum(map(int, str(i))) # map을 사용하는 방법도 있다.

import sys

n = int(sys.stdin.readline())
for i in range(1, n+1):
    constr = sum(int(digit) for digit in str(i)) + i
    if (constr == n):
        print(i)
        break
    if (i == n):
        print(0)
