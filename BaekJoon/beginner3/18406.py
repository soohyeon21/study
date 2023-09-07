# 18406

import sys

n = sys.stdin.readline().rstrip()

left = sum(int(numl) for numl in n[:len(n)//2])
right = sum(int(numr) for numr in n[len(n)//2:])

if (left == right):
    print("LUCKY")
else:
    print("READY")
