# 5929

# a = {1, 2, 3}
# b = {3, 4, 5}
# a&b # {3} # 교집합

import sys

base2 = sys.stdin.readline().rstrip()
base3 = sys.stdin.readline().rstrip()

possible2 = []
for i in range(len(base2)):
    cand = base2[:i] + str(1 - int(base2[i])) + base2[i+1:]
    possible2.append(int(cand, 2))

possible3 = []
for j in range(len(base3)):
    for chance in [0, 1, 2]:
        if (base3[j] != str(chance)):
            cand = base3[:j] + str(chance) + base3[j+1:]
            possible3.append(int(cand, 3))

for one in possible2:
    if (one in possible3):
        print(one)
        break
