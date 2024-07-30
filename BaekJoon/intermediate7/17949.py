# 17949

import sys

cyp = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline())
ntype = sys.stdin.readline().split()

before = 0
result = []
for nt in ntype:
    if (nt == "char"):
        result.append(int(cyp[before:before+2], 16))
        before += 2
    elif (nt == "int"):
        result.append(int(cyp[before:before+8], 16))
        before += 8
    elif (nt == "long_long"):
        result.append(int(cyp[before:before+16], 16))
        before += 16

print(*result)
