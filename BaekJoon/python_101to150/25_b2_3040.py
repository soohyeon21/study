# 3040

# from itertools import permutations, combinations
# permutation: 순열
# combination: 조합

import sys

fake = []
for _ in range(9):
    fake.append(int(sys.stdin.readline()))

suspect = sum(fake) - 100
##print(sum(fake), suspect)

criminal1, criminal2 = 0, 0
for i in range(8):
    for j in range(1, 9):
        if ((fake[i] + fake[j]) == suspect):
            criminal1 = fake[i]
            criminal2 = fake[j]
            break
    if (criminal1 != 0):
        break

##print(criminal1, criminal2)
for gnome in fake:
    if ((gnome != criminal1) and (gnome != criminal2)):
        print(gnome)
