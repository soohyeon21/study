# 23805

import sys

n = int(sys.stdin.readline())

for a1 in range(n):
    print("@"*3*n+" "*n+"@"*n)
for a2 in range(n*3):
    print("@"*n+" "*n+"@"*n+" "*n+"@"*n)
for a3 in range(n):
    print("@"*n+" "*n+"@"*3*n)
