# 1747

# 1,000,000 보다 크거나 같으면서 소수인 수는 1,003,001이다.
# 처음에 소수를 모두 찾아놓고 시작하는 방법 말고도, 매번 해당 수가 소수인지 isPrime() def로 판단하는 방법도 있다.

import sys

n = int(sys.stdin.readline())
max_n = 1003001

num = [True for _ in range(max_n+1)]
num[0], num[1] = False, False
for i in range(2, int(max_n**0.5)+1):
    for j in range(2, max_n//i+1):
        num[i*j] = False

for k in range(n, max_n+1):
    if ((str(k) == str(k)[::-1]) and (num[k] is True)):
        print(k)
        break
