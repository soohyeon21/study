# 2711

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    place, spell = sys.stdin.readline().split()
    place = int(place)
    advised = spell[:place - 1] + spell[place:]
    print(advised)
