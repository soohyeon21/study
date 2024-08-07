# 1990

# 10,000,000(천만) 이상의 소수이면서 팰린드롬 수는 존재하지 않는다.

# 소수를 구하고 팰린드롬을 구하는 것보다, 팰린드롬을 구하고 소수를 구하는 방법이 더 빠르다.
# 팰린드롬 수가 소수보다 더 적기 때문.

import sys

def isPrime(num):
    for i in range(2, int(num**0.5)+1):
        if (num%i == 0):
            return False
    return True


a, b = map(int, sys.stdin.readline().split())
b = min(b, 10**7)

palindrome = [num for num in range(a, b+1) if str(num)==str(num)[::-1]]
for palin in palindrome:
    if (isPrime(palin)):
        print(palin)

print(-1)
