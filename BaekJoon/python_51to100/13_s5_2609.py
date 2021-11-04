# 2609

def GCF2(a, b): # using while
    while (b != 0):
        r = a % b
        a = b
        b = r
    return a

def GCF(a, b): # using recursive function
    return GCF(b, a % b) if b else a

def LCM(a, b):
    return a * b // GCF(a, b)


import sys

a, b = map(int, sys.stdin.readline().split())

print(GCF(a, b))
print(LCM(a, b))
##print(GCF2(a, b))
