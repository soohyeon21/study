# 4796

import sys

idx = 1
while (1):
    l, p, v = map(int, sys.stdin.readline().split())
    if (l == 0):
        break

    use = v//p * l + min(v%p, l)
    
    print(f"Case {idx}: {use}")
    idx += 1
