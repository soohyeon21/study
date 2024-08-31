# 17269

import sys

stroke = {'A': 3, 'B': 2, 'C': 1, 'D': 2, 'E': 4, 'F': 3, 'G': 1, 'H': 3, 'I': 1, 'J': 1, 'K': 3, 'L': 1, 'M': 3, 'N': 2, 'O': 1, 'P': 2, 'Q': 2, 'R': 2, 'S': 1, 'T': 2, 'U': 1, 'V': 1, 'W': 1, 'X': 2, 'Y': 2, 'Z': 1}

n, m = map(int, sys.stdin.readline().split())
names = sys.stdin.readline().split()

two = ""
for i in range(min(len(names[0]), len(names[1]))):
    two += names[0][i]+names[1][i]

if (len(names[0]) < len(names[1])):
    two += names[1][len(names[0]):]
else:
    two += names[0][len(names[1]):]

perc = [stroke[s] for s in two]
while (len(perc) != 2):
    perc2 = [(perc[k]+perc[k+1])%10 for k in range(len(perc)-1)]
    perc = perc2

print(f"{int(''.join(map(str, perc)))}%")
