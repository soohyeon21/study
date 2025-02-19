# 19947

# 틀림

import sys

h, y = map(int, sys.stdin.readline().split())

caseA = h
for ia in range(y//1):
    caseA = int(caseA*(1+0.05))

caseB = h
for ib in range(y//3):
    caseB = int(caseB*(1+0.20))

caseC = h
for ic in range(y//5):
    caseC = int(caseC*(1+0.35))

print(max(caseA, caseB, caseC))
