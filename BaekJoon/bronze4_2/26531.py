# 26531

import sys

equ = sys.stdin.readline().split()
if (int(equ[0])+int(equ[2]) == int(equ[-1])):
    print("YES")
else:
    print("NO")
