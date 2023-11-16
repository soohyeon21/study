# 12813

# 자릿수도 맞춰줘야 함.

# python에서 not 연산하기

import sys

a = int(sys.stdin.readline().rstrip(), 2)
b = int(sys.stdin.readline().rstrip(), 2)
n = 100000
notcal = 2**n - 1

print(bin(a&b)[2:].zfill(n))
print(bin(a|b)[2:].zfill(n))
print(bin(a^b)[2:].zfill(n))
print(f"{a^notcal:0{n}b}")
print(bin(b^notcal)[2:].zfill(n))
