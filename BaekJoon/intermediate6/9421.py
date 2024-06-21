# 9421

# 10**6까지의 소수 말고, 입력한 n까지의 소수만 구해도 충분.

import sys

n = int(sys.stdin.readline())

# 소수 구하기
pnum = [True for _ in range(n+1)] # range(10**6+1)
pnum[0], pnum[1] = False, False
for i in range(2, int(n**0.5)+1): # range(2, int((10)**3)+1)
    for j in range(2, n//i + 1): # range(2, 10**6//i + 1)
        pnum[i*j] = False

# n 이하의 소수상근수 구하기
for target in range(2, n+1):
    if (pnum[target]): # is prime
        already = []
        num = target
        while (1):
            num = str(num)
            nsum = sum(int(digit)**2 for digit in num)
            if (nsum in already):
                break
            elif (nsum == 1):
                print(target)
                break
            else:
                already.append(nsum)
            num = nsum
