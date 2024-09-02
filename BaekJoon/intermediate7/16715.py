# 16715

import sys

def baseSum(num, base):
    changed = []
    while (num != 0):
        changed = [num%base] + changed
        num //= base
    return sum(changed)


n = int(sys.stdin.readline())
dsum = sorted([(base, baseSum(n, base)) for base in range(2, n+1)], key=lambda x:(-x[1], x[0]))

print(dsum[0][1], dsum[0][0])
