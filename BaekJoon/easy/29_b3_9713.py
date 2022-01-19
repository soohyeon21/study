# 9713

# 1부터 n까지의 모든 자연수의 합: 2*(n**2) + n
# n이 짝수일 때,
# 1부터 n까지 수 중 홀수의 합: n**2
# 1부터 n까지 수 중 짝수의 합: n**2 + n

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    k = (n+1) // 2
    print(k**2)
