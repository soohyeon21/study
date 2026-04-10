# 31609

import sys

n = int(sys.stdin.readline())
num = sorted(list(set(map(int, sys.stdin.readline().split()))))

print(*num, sep='\n')
