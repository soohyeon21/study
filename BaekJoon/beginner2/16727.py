# 16727

import sys

p1, e1 = map(int, sys.stdin.readline().split())
e2, p2 = map(int, sys.stdin.readline().split())

winner = ""
if (p1+p2 > e1+e2):
    winner = "Persepolis"
elif (p1+p2 < e1+e2):
    winner = "Esteghlal"
elif (p1+p2 == e1+e2):
    if (e1 > p2):
        winner = "Esteghlal"
    elif (e1 < p2):
        winner = "Persepolis"
    elif (e1 == p2):
        winner = "Penalty"

print(winner)
