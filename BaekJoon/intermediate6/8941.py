# 8941

# max(float(many), 1) # atom이 1개만 있는 경우 처리

import sys

n = int(sys.stdin.readline())

mass = {"C":12.01, 'H':1.008, 'O':16.00, 'N':14.01}

for _ in range(n):
    comp = sys.stdin.readline().rstrip()
    atom = comp[0]
    many = "0"
    total = 0
    for i in range(1, len(comp)):
        if (comp[i].isalpha()):
            total += mass[atom] * max(float(many), 1)
            atom = comp[i]
            many = "0"
        else:
            many += comp[i]
    total += mass[atom] * max(float(many), 1)
    print(f"{total:.3f}")
