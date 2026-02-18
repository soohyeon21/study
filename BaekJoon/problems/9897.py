# 9897

import sys

l, g, r = map(int, sys.stdin.readline().split())

guard = {}
for i1 in range(g):
    who, a, d = sys.stdin.readline().split()
    guard[who] = (int(a), int(d))

light = {i:False for i in range(1, l+1)}
for i2 in range(r):
    man = sys.stdin.readline().rstrip()
    a, d = guard[man]
    for p in range((l-a)//d+1):
        light[a+d*p] = not light[a+d*p]

print(sum(light.values()))
