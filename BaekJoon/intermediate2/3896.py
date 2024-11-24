# 3896

## 소수를 구하는 또 다른 방법. 더 빠름.
# MAX = 1299710
# prime = [True] * MAX
# for i in range(2, MAX):
#   if (prime[i]):
#       for j in range(i*i, MAX, i): # for j in range(i+i, MAX+1, i):
#           prime[j] = False

import sys

t = int(sys.stdin.readline())

prime = [True for x in range(1299710)]
prime[0], prime[1] = False, False
for i in range(2, int(1299709**0.5)+1):
    for j in range(2, 1299709//i+1):
        prime[i*j] = False

for _ in range(t):
    k = int(sys.stdin.readline())
    if (prime[k]):
        print(0)
        continue
    
    right, left = 0, 0
    for r in range(k+1, 1299710):
        if (prime[r]):
            right = r
            break
    for l in reversed(range(2, k)):
        if (prime[l]):
            left = l
            break
    print(right - left)
