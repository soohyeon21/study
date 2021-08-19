# 2581

# print(list.sort())의 결과는 None이다.
# sort()는 원본 변경.
# sort 대신 min() 사용 가능. 10ms 정도 save.

import math

m = int(input())
n = int(input())

prime = []

for num in range(m, (n + 1)):
    if (num == 1):
        continue
    if (num == 2):
        prime.append(num)
    cnt = 0
    for i in range(1, (math.ceil(math.sqrt(num)) + 1)):
        if (num % i == 0):
            cnt += 1
    if (cnt == 1):
        prime.append(num)
#print(prime)
if (prime == []): # len(prime) == 0
    print(-1)
else:
    print(sum(prime))
    print(min(prime))
##    prime.sort()
##    print(sum(prime))
##    print(prime[0])
