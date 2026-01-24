# 35149

# 사실 stage를 다 합쳐서 하나로 만들었어도 괜찮았다.

import sys

n, m = map(int, sys.stdin.readline().split())
stage = [sys.stdin.readline().rstrip() for _ in range(n)]

level = 4

wall = 0
oned = 0
alld = 0
vaccine = 0
start, end = 0, 0
for eachs in stage:
    wall += eachs.count('#')
    for onev in 'UDLR':
        oned += eachs.count(onev)
    alld += eachs.count('A')
    vaccine += eachs.count('V')
    start += eachs.count('S')
    end += eachs.count('E')

if (alld == 0):
    level = 3
if ((alld == 0) and (vaccine == 0)):
    level = 2
if ((wall <= 1) and (oned <= 1) and (alld == 0) and (vaccine == 0)):
    level = 1
if ((start != 1) or (end != 1)):
    level = -1

print(level)
