# 14563

import sys

t = int(sys.stdin.readline())
nlist = list(map(int, sys.stdin.readline().split()))
for num in nlist:
    factor = []
    for i in range(1, int(num**0.5)+1):
        if (num%i == 0):
            factor.append(i)
            if (num//i not in factor):
                factor.append(num//i)

    if (sum(factor) == num*2):
        print("Perfect")
    elif (sum(factor)-num < num):
        print("Deficient")
    else:
        print("Abundant")
