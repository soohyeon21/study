# 11922

import sys

n, b = sys.stdin.readline().split()
same = {"A":11, "K":4, "Q":3, "8":0, "7":0, "T":10}
slist = "AKQ87T"
domin = {"J":20, "9":14}
ndomin = {"J":2, "9":0}
total = 0
for _ in range(4*int(n)):
    card = sys.stdin.readline().rstrip()
    if (card[0] in slist):
        total += same[card[0]]
    elif (card[1] == b):
        total += domin[card[0]]
    else:
        total += ndomin[card[0]]
print(total)
