# 8760

# (w//2 * k + w%2 * k//2)
# (k//2 * w + k%2 * w//2)
# (w*k//2) # 어떻게든 알아서 잘 인접한 2개가 선택될 수 있나보다.

import sys

z = int(sys.stdin.readline())

for _ in range(z):
    w, k = map(int, sys.stdin.readline().split())
    print(w*k//2)
