# 11653

# 합성수: 두 개 이상의 소수의 곱으로 이루어진 수.
# 따라서, 소수와 소수의 곱은 소수가 될 수 없다.

# 사실 sqrt()만 넘어가면, 짝이 지어져 있어서 그거 출력하면 됨.
# 소인수 2개로 이루어진 합성수면, 해당 소인수 2개 외의 조합을 만들어낼 수 없음.

# 'n /= k'도 되고, 'n //= k'도 됨. like 'n += 1'

# 시간 초과 code에서 수정.
import math

n = int(input())
prime = []

# find prime
for num in range(1, (math.ceil(math.sqrt(n)) + 1)):
    if (num == 1):
        continue
    if (num == 2):
        prime.append(num)
        continue
    cnt = 0
    for i in range(1, (math.ceil(math.sqrt(num)) + 1)):
        if (num % i == 0):
            cnt += 1
    if (cnt == 1):
        prime.append(num)
#print(prime)

# find prime factor
for fac in prime:
    while (n % fac == 0):
        n //= fac # or 'n /= fac'하고 밑에서 'print(int(n))'
        print(fac)
if (n != 1):
    print(n)
