# 19698

# 헛간이 모든 소들이 들어가고도 남을 만큼 널널할 수도 있다.
# min(n, many)

import sys

n, w, h, l = map(int, sys.stdin.readline().split())
many = (w//l) * (h//l)
if (many > n):
    print(n)
else:
    print(many)
