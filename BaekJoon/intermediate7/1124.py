# 1124

import sys

a, b = map(int, sys.stdin.readline().split())

primes = [True]*(b+1)
primes[0], primes[1] = False, False
for i in range(2, int(b**0.5)+1):
    for j in range(2, b//i+1):
        primes[i*j] = False

under_cnt = 0
# a~b 사이의 정수 중에서
for num in range(a, b+1):
    prime_cnt = 0
    rest = num
    # 해당 정수 이하의 소수 중에서
    for check in range(2, num+1):
        # 소인수이면
        if ((num%check == 0) and (primes[check])):
            while (rest%check != 1):
                if (rest%check != 0):
                    break
                prime_cnt += 1
                rest //= check

    # 언더프라임인지 확인
    if (primes[prime_cnt]):
        under_cnt += 1

print(under_cnt)
