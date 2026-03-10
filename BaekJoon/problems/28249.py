# 28249

import sys

pepper = {'Poblano':1500, 'Mirasol':6000, 'Serrano':15500, 'Cayenne':40000, 'Thai':75000, 'Habanero':125000}

t = int(sys.stdin.readline())

total = 0
for _ in range(t):
    pep = sys.stdin.readline().rstrip()
    total += pepper[pep]

print(total)
