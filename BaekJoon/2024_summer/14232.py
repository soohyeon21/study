# 14232

# k까지의 소수를 구하고, 그 중에서 소인수를 구해 소인수분해 하는 것은 메모리 초과

# math.sqrt(k)보다 큰 수 중에서 소인수는 무조건 1개이거나 0개라고 한다.

import sys

k = int(sys.stdin.readline())

weight = []
for i in range(2, int(k**0.5)+1):
    while (k%i == 0):
        weight.append(i)
        k //= i

if (k != 1):
    weight.append(k)
    

print(len(weight))
print(*sorted(weight))
