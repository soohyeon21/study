# 4589

import sys

n = int(sys.stdin.readline())

print("Gnomes:")

for _ in range(n):
    gnome = list(map(int, sys.stdin.readline().split()))
    if ((gnome == sorted(gnome)) or (gnome == sorted(gnome, reverse=True))):
        print("Ordered")
    else:
        print("Unordered")
