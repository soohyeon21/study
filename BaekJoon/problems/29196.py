# 29196

# "p,q는 10**9 이하인 양의 정수"
# "k는 최대 소수점 아래 여덟 자리까지 주어짐"

import sys

k = sys.stdin.readline().rstrip()

zeros = len(k[2:])

print("YES")
print(int(k[2:]), 10**zeros)
