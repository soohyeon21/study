# 2090

# a = [1, 2, 3], math.lcm(*a), sum(a)

import sys

def gcf(a, b):
    while (b != 0):
        num = a%b
        a = b
        b = num
    return a

def lcm(a, b):
    return a*b//gcf(a, b)


n = int(sys.stdin.readline())
an = list(map(int, sys.stdin.readline().split()))

denom = 1
for i in range(n):
    denom = lcm(denom, an[i])
numer = sum(denom//each for each in an)

gcf_dn = gcf(denom, numer)

print(f"{denom//gcf_dn}/{numer//gcf_dn}")
