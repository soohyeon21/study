# 19945

# n < 0 일때는 32 # (-2,147,483,648<=n)이기 때문
# n > 0 일때는 len(bin(n))-2

import sys

n = int(sys.stdin.readline())

decn = 0
if (n >= 0):
    decn = int(bin(n)[2:])
if (n < 0):
    comp1 = '0b'+''.join([str(abs(int(digit)-1)) for digit in bin(n)[3:].zfill(32)])
    comp2 = bin(int(comp1, 2) + 1)[2:]
    decn = int(comp2)

length = len(str(decn))
print(length)
