# 20017

import sys

n, m, a = map(int, sys.stdin.readline().split())
cats = list(map(int, sys.stdin.readline().split()))

fine = 0
for floor in range(n-1):
    for door in range(m):
        if (2*cats[floor*m + door] < cats[(floor+1)*m + door]):
            fine += a

print(fine)
