# 23808

import sys

n = int(sys.stdin.readline())

for a1 in range(2*n):
    print("@"*n+" "*3*n+"@"*n)
for a2 in range(n):
    print("@"*5*n)
for a3 in range(n):
    print("@"*n+" "*3*n+"@"*n)
for a4 in range(n):
    print("@"*5*n)
