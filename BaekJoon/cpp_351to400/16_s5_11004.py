# 11004

# python의 sort()는 Tim Sort.

import sys

n, k = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
num.sort()

print(num[k-1])
