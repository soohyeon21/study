# 31775

import sys

cheer = set()
for _ in range(3):
    word = sys.stdin.readline().rstrip()
    cheer.add(word[0])

if (cheer == {'l', 'k', 'p'}):
    print("GLOBAL")
else:
    print("PONIX")
