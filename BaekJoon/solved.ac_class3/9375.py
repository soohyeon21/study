# 9375

# clothes에 굳이 name 말고 그냥 개수만 세어도 되었을듯.
# 굳이 len(ditems)에 따라 경우 나누지 않아도 되었을듯.

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    clothes = {}
    for i in range(n):
        name, typee = sys.stdin.readline().split()
        clothes[typee] = clothes.setdefault(typee, [])
        clothes[typee].append(name)

    ditems = list(clothes.items())
    if (len(ditems) == 1):
        print(len(ditems[0][1]))
    else:
        cnt = 1
        for one in ditems:
            cnt *= len(one[1])+1
        print(cnt - 1)
