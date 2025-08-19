# 7482

# V(b) = 4b**3 - 4ab**2 + a**2b # b에 대한 방적식을 풀면 된다. (b=a/2 or b=a/6)

import sys

n = int(sys.stdin.readline())

for _ in range(n):
    a = float(sys.stdin.readline())
    print(f"{a/6:.10f}")
