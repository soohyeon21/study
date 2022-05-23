# 11945

import sys

n, m = map(int, sys.stdin.readline().split())
for _ in range(n):
    boong = sys.stdin.readline().rstrip()
    print(boong[::-1])
