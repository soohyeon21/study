# 3023

import sys

r, c = map(int, sys.stdin.readline().split())
card = [sys.stdin.readline().rstrip() for row in range(r)]
a, b = map(int, sys.stdin.readline().split())

for i in range(r):
    card.append(card[r-1-i])
for j in range(2*r):
    card[j] = card[j]+card[j][::-1]

a -= 1
b -= 1
if (card[a][b] == "#"):
    change = "."
else:
    change = "#"
card[a] = card[a][:b] + change + card[a][b+1:]

print(*card, sep="\n")
