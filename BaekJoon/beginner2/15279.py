# 15279

import sys

n = int(sys.stdin.readline())
for _ in range(n):
    b, p = map(float, sys.stdin.readline().split())
    abpm = 60/p
    bpm = 60*b/p
    print(f"{bpm-abpm:.4f} {bpm:.4f} {bpm+abpm:.4f}")
