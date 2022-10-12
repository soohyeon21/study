# 10539

# 첫 시도 때, a를 안 구하고 b를 구했다. 문제 제대로 읽자.
# 이 문제도 예상보다는 쉽게 풀었다.

import sys

n = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))
a = [b[0]]

for i in range(1, n):
    a.append((i+1)*b[i] - sum(a))

print(*a)
