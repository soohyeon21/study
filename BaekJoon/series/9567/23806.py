# 23806

import sys

n = int(sys.stdin.readline())

for a1 in range(n):
    print("@"*5*n)
for a2 in range(3*n):
    print("@"*n+" "*n*3+"@"*n)
for a3 in range(n):
    print("@"*5*n)
