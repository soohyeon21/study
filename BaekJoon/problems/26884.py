# 26884

import sys

n = int(sys.stdin.readline())

artist = {}
for _ in range(n):
    name = sys.stdin.readline().rstrip()
    artist[name] = artist.setdefault(name, 0)
    artist[name] += 1

cnt = 0
for v in artist.values():
    if (v > 1):
        cnt += 1

print(cnt)
