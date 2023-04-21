# 17174

import sys

n, m = map(int, sys.stdin.readline().split())

total = n
while (n >= m):
    total += n//m
    n //= m
    
print(total)
