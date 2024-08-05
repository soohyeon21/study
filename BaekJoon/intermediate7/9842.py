# 9842

# or 10000번째 소수인 104730까지 포함하는 list를 만들어서 에라토스테네스의 체로 for문 2번 사용해서 True/False 표시하기

import sys

def isPrime(number):
    for i in range(2, int(number**0.5)+1):
        if (number % i == 0):
            return False
    return True

prime = [2]

n = int(sys.stdin.readline())

num = 3
while (len(prime) < n):
    if (isPrime(num)):
        prime.append(num)
    num += 1

print(prime[n-1])
