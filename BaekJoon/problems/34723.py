# 34723

# minx의 초기값은 무한대(float('inf')) or abs(x-4)로 해야 한다.

import sys

p, m, c = map(int, sys.stdin.readline().split())
x = int(sys.stdin.readline())

minx = abs(x-4)
for p1 in range(1, p+1):
    for m1 in range(1, m+1):
        for c1 in range(1, c+1):
            minx = min(abs((p1+m1)*(m1+c1)-x), minx)

print(minx)
