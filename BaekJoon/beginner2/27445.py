# 27445

# hor도 [] 안에 for문 넣어서 끝낼 수 있다.

import sys

n, m = map(int, sys.stdin.readline().split())
hor = []
for _ in range(n-1):
    hor.append(int(sys.stdin.readline()))
ver = list(map(int, sys.stdin.readline().split()))
hor.append(ver[0])
print(hor.index(min(hor))+1, ver.index(min(ver))+1)
