# 32068

# (L < S < R) 이므로 1단계에서 보물찾기가 종료되는 경우는 없다. max()는 고려하지 않아도 되었다.

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    l, r, s = map(int, sys.stdin.readline().split())
    left = abs(l-s)
    right = abs(r-s)

    tre_right = 2*right
    tre_left = 2*left+1
    last = max(1, min(tre_left, tre_right))

    print(last)
