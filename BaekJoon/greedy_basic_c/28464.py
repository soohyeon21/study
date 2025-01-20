# 28464

import sys

n = int(sys.stdin.readline())
an = sorted(list(map(int, sys.stdin.readline().split())))

park = sum(an[n//2:])
sung = sum(an[:n//2])

print(sung, park)
