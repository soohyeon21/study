# 15372

# N이 주어질때, N의 제곱의 수 중에서 가장 작은 양의 정수인 수가 무엇인지 구하라
# == N을 제곱한 수를 출력하라
# 문제를 꼬아서 적어놓은 것 같다.

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    print(n**2)
