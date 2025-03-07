# 6219

import sys

a, b, d = map(int, sys.stdin.readline().split())

primes = [1 for i in range(4000001)] # True, range(b+1)는 시간에 영향 미미. 100~200ms 정도.
primes[0], primes[1] = 0, 0

for j in range(2, int(b**0.5)+1):
##    for k in range(2, b//j+1):
##        primes[j*k] = 0
    for k in range(2*j, b+1, j): # 1000ms faster
        primes[k] = 0

cnt = 0
for num in range(a, b+1):
    if (primes[num] and (str(d) in str(num))):
        cnt += 1

print(cnt)
