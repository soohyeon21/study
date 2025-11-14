# 2986

# 본인 제외 가장 큰 약수를 구하는 문제

# 굳이 n**0.5 이하의 모든 소수를 구할 필요 없다. 그러다가 메모리 초과 발생함.
# 굳이 n=1인 경우를 분리해서 생각하지 않아도 된다.

import sys

n = int(sys.stdin.readline())

gf = 1
for k in range(2, int(n**0.5)+1):
    if (n%k == 0):
        gf = n//k
        break

print(n-gf)
